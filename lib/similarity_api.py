from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import pandas as pd
import numpy as np
import os
from dotenv import find_dotenv, load_dotenv
from pinecone import create_index, list_indexes, Index, init

# Initialize the Flask app
# Flask is a web application framework written in Python
flask_app = Flask(__name__)
flask_app.debug = True
flask_app.use_reloader = True

# define our embedding model
model = SentenceTransformer('bert-base-nli-mean-tokens')

# get our pinecone_api_key from the environment variable
# Load environment variables from .env file
load_dotenv(find_dotenv())

# Set API credentials as variables => Please make sure you have a .env file with the following variables
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
PINECONE_ENV = os.environ["PINECONE_ENV"]

# initialize our pinecone index
# connect to our pinecone instance
init(
    api_key=PINECONE_API_KEY, 
    environment=PINECONE_ENV
)

# Create a pincone index

if "companies" not in list_indexes():
    create_index(name="companies", metric="cosine", shards=1, dimension=768)
# list_indexes()
index = Index("companies")

# Search for the top 5 most similar companies
def pinecone_search(index, query):
    # create the query vector
    xq = model.encode(query).tolist()
    results = index.query(xq, top_k=3, include_metadata=True)
    return results

@flask_app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == 'GET':
        # get the search query from the request and return the top 5 results
        query = request.json["query"].strip()
        print('searching: ' + query)        
        res = pinecone_search(index, query)
        # get the matches from res
        matches = res["matches"]        
        # print(matches)
        # create a json from the matches with the company name, description and the similarity score
        results = []
        for match in matches:
            results.append({
                "company": match["metadata"]["name"],
                "description": match["metadata"]["description"],
                "score": match["score"]
            })
        return results


# Run the Flask app
if __name__ == "__main__":
    flask_app.run(port=8000)
