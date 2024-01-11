from flask import Flask, request
import pickle
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

meds = pd.read_csv('../out.csv')

with open('knn_model.pkl', 'rb') as file:
    knn = pickle.load(file)

embedder = SentenceTransformer('msmarco-distilbert-base-v4')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index_handler():
    return "<p>Hello, World!</p>"

@app.route("/search", methods=['POST'])
def search():
    data = request.json()

    test_prompt = embedder.encode(data.query).astype(np.float32)
    distances, indices = knn.kneighbors([test_prompt])

    nnbrs = []
    for i in indices[0]:
        nnbrs.append({
            'name': meds.at[i, 'Medicine name'],
            'Therapeutic area': meds.at[i, 'Therapeutic area'],
            'Condition / indication': meds.at[i, 'Condition / indication'],
            'URL': meds.at[i, 'URL']            
        })

    return nnbrs

@app.route("/id/<int:id>", methods=['GET'])
def id_handler(id):
    if id > len(meds):
        return {
            'name': '',
            'Therapeutic area': '',
            'Condition / indication': '',
            'URL': ''
        }

    return {
        'name': meds.at[id, 'Medicine name'],
        'Therapeutic area': meds.at[id, 'Therapeutic area'],
        'Condition / indication': meds.at[id, 'Condition / indication'],
        'URL': meds.at[id, 'URL']
    }
