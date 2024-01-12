# %%
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
# %%
meds = pd.read_csv('../medicines_output_european_public_assessment_reports_en.csv')
meds.head()
# %%
indications = meds['Condition / indication']
embedder = SentenceTransformer('msmarco-distilbert-base-v4')
embeddings = embedder.encode(indications).astype(np.float32)
# %%
meds['indication embedding'] = pd.Series(embeddings.tolist())
meds.to_csv('../out.csv')
# %%)
k = 5
knn = NearestNeighbors(n_neighbors=k)
knn.fit(embeddings)
# %%
test_prompt = embedder.encode("relapsing remitting multiple sclerosis").astype(np.float32)
distances, indices = knn.kneighbors([test_prompt])
print('Nearest neighbors: ', indices)
print('Distances: ', distances)
# %%
import pickle

# Save the fitted model to a file using pickle
with open('knn_model.pkl', 'wb') as file:
    pickle.dump(knn, file)