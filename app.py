import pickle
import spacy
import random
from flask import Flask, render_template

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/"

train_data = pickle.load(open('training_files/train_data.pkl', 'rb'))

nlp = spacy.blank('en')


def train_model(train_data):
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)

    for _, annotation in train_data:
        for ent in annotation['entities']:
            ner.add_label(ent[2])

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(10):
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)