import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

def load_data():
    df = pd.read_csv("data.csv")
    return df

def preprocess_data(df):
    X = df.drop(columns=["target"])
    y = df["target"]
    return train_test_split(X, y, test_size=0.2)

def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def save_model(model):
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
