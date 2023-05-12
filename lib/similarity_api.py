from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import pandas as pd
import numpy as np


# Initialize the Flask app
# Flask is a web application framework written in Python
flask_app = Flask(__name__)
flask_app.debug = True
flask_app.use_reloader = True

model = SentenceTransformer('bert-base-nli-mean-tokens')

print('Training model...')
file_path='./data/companies_10000_internet.csv'
# load the data
print('Loading data...')
df = pd.read_csv(file_path)
print('Data loaded: ', df.shape)
sentences = df['description'].tolist()
# encode the descriptions
print('Encoding descriptions...')
embeddings = model.encode(sentences)
print('Descriptions encoded: ', len(embeddings))
# calculate the similarity matrix
print('Calculating similarity matrix...')
sim = np.zeros((len(sentences), len(sentences)))
for i in range(len(sentences)):
    sim[i:,i] = cos_sim(embeddings[i], embeddings[i:])
print('Similarity matrix calculated: ', sim.shape)
print('Model trained!')

# given 2 company names, return the similarity score
# get_similarity_score('AccountPal', 'Ubiquity NZ')
def get_similarity_score(company1, company2, df):
    index1 = df[df['name'] == company1].index[0]
    index2 = df[df['name'] == company2].index[0]
    # if one of the 2 companies is not in the list, return 0
    if index1 == -1 or index2 == -1:
        return 0
    return sim[index1, index2]


# for a given company, find the top 5 most similar companies
# find_similar_companies('AccountPal', sim, sentences)
def find_similar_companies(company_name, sim, sentences, top_n=5):
    # if the company is not in the list, return empty list
    if company_name not in df['name'].tolist():
        return []
    sentence = df[df['name'] == company_name]['description'].tolist()[0]
    idx = sentences.index(sentence)
    top_n_idx = np.argsort(sim[idx,:])[-top_n:][::-1]
    res = []
    for i in top_n_idx:
        if sim[idx,i] >= 0.3:
            res.append((df['name'][i],sentences[i], sim[idx,i]))
    return res

# search for a company based on a sentence using the sim matrix
# search_company('account based marketing', sim, sentences)
def search_company(sentence, sim, sentences, top_n=5):
    sentence_embedding = model.encode([sentence])
    sim_score = np.zeros(len(sentences))
    for i in range(len(sentences)):
        sim_score[i] = cos_sim(sentence_embedding, embeddings[i])
    top_n_idx = np.argsort(sim_score)[-top_n:][::-1]
    res = []
    for i in top_n_idx:
        if sim_score[i] >= 0.3:
            res.append((df['name'][i],sentences[i], sim_score[i]))
    if len(res) == 0:
        return [('No result found', '', 0)]
    return res



@flask_app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == 'GET':
        # get the search query from the request and return the top 5 results
        query = request.json["query"].strip()
        print('searching:' + query)
        print('within '+str(len(sentences))+' companies')
        res = search_company(query, sim, sentences)
        print(res)
        return jsonify(res)
    
@flask_app.route("/compare", methods=["GET", "POST"])
def compare():
    if request.method == 'GET':
        # compare 2 companies and return the similarity score
        company1 = request.json["company1"].strip()
        company2 = request.json["company2"].strip()
        print('comparing: ' + company1 + ' and ' + company2)
        score = get_similarity_score(company1, company2, df)
        print(score)
        return jsonify(score)
    
    


# Run the Flask app
if __name__ == "__main__":
    flask_app.run(port=8000)
