import pandas as pd

data = [
    [0.8, 1.0, 80, 2, 85],
    [0.6, 0.8, 60, 1, 70],
    [0.3, 0.5, 40, 0.5, 50],
    [0.9, 1.0, 90, 3, 95],
    [0.4, 0.6, 50, 1, 60],
]

df = pd.DataFrame(data, columns=[
    "similarity", "skill", "keyword", "experience", "score"
])

from sklearn.linear_model import LinearRegression

X = df[["similarity", "skill", "keyword", "experience"]]
y = df["score"]

model = LinearRegression()
model.fit(X, y)

import pickle


with open("model.pkl", "wb") as f:
    pickle.dump(model, f)