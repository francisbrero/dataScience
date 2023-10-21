import requests
from dotenv import load_dotenv
load_dotenv()
import os

# get the credentials from our .env file
api_key = os.getenv('seg_api_key')
cx = os.getenv('seg_cx')


def query_seg(query):
  """Queries the Google Custom Search Engine API and returns the results."""

  url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}".format(api_key, cx, query)

  response = requests.get(url)

  if response.status_code == 200:
    results = response.json()["items"]
    for result in results:
      print(result["title"])
      print(result["link"])
  else:
    print("Error: {}".format(response.status_code))

if __name__ == "__main__":
  query = input("Enter a search query: ")
  query_seg(query)