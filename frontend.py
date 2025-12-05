import streamlit as st
import requests

st.set_page_config(page_title="AI Business Analyst Agent", layout="centered")

st.title("📊 AI Business Data Analyst Agent")
st.write("Upload your sales data and ask business questions in plain English.")

API_URL = "http://127.0.0.1:8000"

# ---------- CSV Upload ----------
st.header("📁 Upload Sales CSV")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{API_URL}/upload_csv", files={"file": uploaded_file})

    if response.status_code == 200:
        data = response.json()
        st.success(f"✅ File Uploaded | Rows: {data['rows']} | Columns: {len(data['columns'])}")
        st.write("Columns:", data["columns"])
    else:
        st.error("❌ File upload failed")

# ---------- ML Prediction ----------
st.header("📈 Predict Sales")

month = st.number_input("Enter Month (1–12)", min_value=1, max_value=12)
day = st.number_input("Enter Day (1–31)", min_value=1, max_value=31)

if st.button("Predict"):
    params = {"month": month, "day": day}
    res = requests.post(f"{API_URL}/predict", params=params)

    if res.status_code == 200:
        st.success(f"💰 Predicted Sales: {res.json()['predicted_sales']:.2f}")
    else:
        st.error("❌ Prediction failed")

# ---------- Ask Business Questions ----------
st.header("💬 Ask Business Questions")

question = st.text_input("Ask like: Total sales? Highest sales? Average sales?")

if st.button("Ask AI Agent"):
    params = {"question": question}
    res = requests.post(f"{API_URL}/ask", params=params)

    if res.status_code == 200:
        st.info(res.json()["answer"])
    else:
        st.error("❌ AI Agent failed to respond")
