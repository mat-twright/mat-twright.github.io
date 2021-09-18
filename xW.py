
import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('data.csv')

X = data.iloc[:, [0, 1, 2, 3, 4]]
y = data.iloc[:, 5]

print(X)

clf = RandomForestClassifier()
clf.fit(X, y)

results = clf.predict_proba(X.iloc[:, [0, 1, 2, 3, 4]])

out = {}

for i, j in enumerate(results):
  try:
    out[i//7] += j[1]
  except:
    out[i//7] = j[1]

print(out)
