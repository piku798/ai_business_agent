import pandas as pd
import joblib
import shutil

from fastapi import FastAPI, UploadFile, File
from agent import agent_answer
from utils import clean_data

app = FastAPI()

# Load model
model = joblib.load("models/sales_model.pkl")


@app.get("/")
def home():
    return {"message": "AI Business Agent Running"}


@app.post("/upload_csv")
def upload_csv(file: UploadFile = File(...)):
    with open("data/uploaded.csv", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    df = pd.read_csv("data/uploaded.csv")
    df = clean_data(df)

    return {
        "rows": len(df),
        "columns": list(df.columns)
    }


@app.post("/predict")
def predict(month: int, day: int):
    pred = model.predict([[month, day]])
    return {"predicted_sales": float(pred[0])}


@app.post("/ask")
def ask(question: str):
    answer = agent_answer(question)
    return {"answer": answer}
