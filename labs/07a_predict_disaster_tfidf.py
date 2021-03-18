#!/usr/bin/env python
# coding: utf-8

from disaster_detection_tfidf import clf
import numpy as np
import pandas as pd
import pickle
from rich import print

# queries are stored in the variable query_text
query_text = pd.read_csv('./disaster_data/predict.csv').text.values

with open('vectorizer.pk', 'rb') as fin:
    vectorizer= pickle.load(fin)

with open('clf.pk', 'rb') as fin:
    clf = pickle.load(fin)


def predict(model, query_txt):
    x = vectorizer.transform([query_txt]).toarray()
    pred = model.predict(x)
    if pred[0] == 1:
        print(f"[red]{query_txt} -> Disaster")
    else:
        print (f"[green]{query_txt} -> Not a disaster")


for query in query_text:
    predict (clf, query)

