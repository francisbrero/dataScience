# Data Science
A quick repo to remember the stuff I'm working on...

# Configure
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
