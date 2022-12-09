from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import spacy
import pickle
import random
import sys, fitz
from tabulate import tabulate
from prettytable import PrettyTable
import docx2txt
import pathlib

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"

train_data = pickle.load(open('training_files/train_data.pkl', 'rb'))

nlp = spacy.blank('en')

def train_model(train_data):
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last = True)
    
    for _, annotation in train_data:
        for ent in annotation['entities']:
            ner.add_label(ent[2])
            
    
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(2):
            print("Starting iteration " + str(itn))
            random.shuffle(train_data)
            losses = {}
            index = 0
            for text, annotations in train_data:
                try:
                    nlp.update(
                        [text],  # batch of texts
                        [annotations],  # batch of annotations
                        drop=0.2,  # dropout - make it harder to memorise data
                        sgd=optimizer,  # callable to update weights
                        losses=losses)
                except Exception as e:
                    pass
                
            print(losses)



train_model(train_data)

nlp.to_disk('training_files/nlp_model')

nlp_model = spacy.load('training_files/nlp_model')

print("train OK----------")


@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file_extension = pathlib.Path(app.config['UPLOAD_FOLDER'] + filename).suffix

        tx = ''
        if file_extension == ".pdf":
            tx = read_pdf(filename)
        elif file_extension == ".txt":
            tx = read_txt(filename)
        elif file_extension == ".docx":
            tx = read_docx(filename)

        t = PrettyTable(['Catalog', 'Value'])

        doc = nlp_model(tx)
        for ent in doc.ents:
            print(ent)
            t.add_row([str(ent.label_.upper()), str(ent.text)])
        
    return render_template('content.html', content=t) 

def read_pdf(filename):
        file = open(app.config['UPLOAD_FOLDER'] + filename, "rb").read()
        doc = fitz.open("pdf", file)

        text = ""
        for page in doc:
            text = text + str(page.get_text())

        tx = " ".join(text.split('\n'))
        return tx

def read_txt(filename):
        file = open(app.config['UPLOAD_FOLDER'] + filename).read()

        tx = ''
        for i in file:
           tx += str(i)
        return tx

def read_docx(filename):
    file = docx2txt.process(app.config['UPLOAD_FOLDER'] + filename)

    tx = ''
    for i in file:
        tx += str(i)
    return tx

if __name__ == '__main__':  
    app.run(host="0.0.0.0", port=5000, debug = True)