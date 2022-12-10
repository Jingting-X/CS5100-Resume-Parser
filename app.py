from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import spacy
import random
from tabulate import tabulate
from prettytable import PrettyTable
import pathlib
from train_model import*
from read_file import*

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"

train_model()

nlp.to_disk('training_files/nlp_model')
nlp_model = spacy.load('training_files/nlp_model')

print("---------Model Training Done---------")

# Get test result
# print("---------Model Testing Report---------")
# test_model_report()


@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/display', methods = ['GET', 'POST'])
def parse_resume():
    if request.method == 'POST':
        f = request.files['file']
        file_name = secure_filename(f.filename)
        file_path = app.config['UPLOAD_FOLDER'] + file_name
        f.save(file_path)
        file_extension = pathlib.Path(file_path).suffix

        file_content = ''
        if file_extension == ".pdf":
            file_content = read_pdf(file_path)
        elif file_extension == ".txt":
            file_content = read_txt(file_path)
        elif file_extension == ".docx":
            file_content = read_docx(file_path)

        t = PrettyTable(['Catalog', 'Value'])
        doc = nlp_model(file_content)
        for ent in doc.ents:
            t.add_row([str(ent.label_.upper()), str(ent.text)])

    return render_template('content.html', content=t)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)
