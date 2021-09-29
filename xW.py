
import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

data = pd.read_csv('data.csv')

X = data.iloc[:, [0, 1, 2, 3, 4]]
y = data.iloc[:, 5]

#clf = RandomForestClassifier()
clf = GaussianNB()
clf.fit(X, y)

'''

results = clf.predict_proba(X.iloc[:, [0, 1, 2, 3, 4]])

out = {}

for i, j in enumerate(results):
  try:
    out[i//7] += j[1]
  except:
    out[i//7] = j[1]

print(out)
'''


sport = 3
location = 2
players = [(0, 1, 0), (1, 1, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0), (5, 1, 0), (6, 1, 2), (7, 0, 1), (8, 2, 2), (9, 0, 0), (10, 0, 0)]
x = []

for player in players:
    x.append(clf.predict_proba(np.array([player[0], sport, location, player[1], player[2]]).reshape(1, -1))[0][1])

s = sum(x)
y = [i/s for i in x]

print(y)
