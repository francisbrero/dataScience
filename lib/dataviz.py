import d3;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

# load csv file into a pandas dataframe
def load_csv(file_name):
    return pd.read_csv(file_name);

# make api call to get data
def get_data(url):
    return d3.json(url);

# make api call with authorization to get data
def get_data_auth(url, auth):
    return d3.json(url, auth=auth);

