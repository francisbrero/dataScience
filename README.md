# Data Science
A quick repo to remember the stuff I'm working on...

# Similarity Funzies
## .env
Rename the .env_sample file to .env and add your Pinecone credentials.
You don't need a paid Pinecone instance for this

## getting started
Run through the company_similarity.ipynb notebook to configure your pinecone index

## Prep the API environment
Let's spin up a virtual environment
``` bash
python3 -m venv env
source env/bin/activate
```
let's install the required libraries on the virtual environment
``` bash
pip install -r requirements.txt
```

## Spin up the API
``` bash
python ./lib/similarity_api.py
```
This spins up a flask app API you can access to query our pinecone index

# Use the API
## Test in postman
In postman, create a HTTP Request: GET + `http://localhost:8000/search`
The body should contain your query, something like 
```json
{
    "query": "collaborative software for engineering teams to create prototypes"
}
```
![image](https://github.com/francisbrero/dataScience/assets/2491181/97125b4d-52c7-4358-9ddf-d464430bf8f7)


# Google Search Engine with GenAI
## Get your keys to write in your .env file

To obtain a Google Custom Search Engine API key and Google Custom Search Engine CX, you will need to:

- Go to the Google Cloud Platform Console.
If you don't already have a Google Cloud Platform project, create one.
- Click the hamburger menu in the top left corner of the page and select APIs & Services.
- Click Enable APIs and Services.
- https://developers.google.com/custom-search/v1/overview
- Search for "Custom Search Engine API" and enable the API.

To obtain a Google Custom Search Engine CX, you will need to:

- Go to the [Programmable Search Engine control panel](https://programmablesearchengine.google.com/controlpanel).
- Click Create a search engine.
- Enter a name for your search engine and click Create.
- On the Basic page, copy the Search engine ID. This is your CX.

# Install and run chroma
## Install chroma
```bash
pip install chroma
```
## Run chroma
```bash
chroma run --path "../data" --port 8000
```
