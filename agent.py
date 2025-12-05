import pandas as pd
from transformers import pipeline

# -------------------- Load Dataset --------------------
df = pd.read_csv(r"C:\Users\nnaya\Desktop\ai_business_agent\data\retail_sales_dataset.csv")

# -------------------- Create Data Summary --------------------
data_summary = f"""
Total Rows: {len(df)}
Columns: {list(df.columns)}
Total Sales: {df['sales'].sum()}
Average Sales: {df['sales'].mean()}
Highest Sales: {df['sales'].max()}
Lowest Sales: {df['sales'].min()}
"""

# -------------------- Load FREE Lightweight LLM --------------------
# IMPORTANT: FLAN-T5 uses "text2text-generation", NOT "text-generation"
llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=150
)

# -------------------- Business Analyst Agent --------------------
def agent_answer(question: str):
    prompt = f"""
You are an expert business data analyst.

Dataset Summary:
{data_summary}

User Question:
{question}

Give a clear business-friendly answer.
"""
    result = llm(prompt)
    return result[0]["generated_text"]
