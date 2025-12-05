import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from utils import clean_data

df = pd.read_csv(r'C:\Users\nnaya\Desktop\ai_business_agent\data\retail_sales_dataset.csv')
df = clean_data(df)

X = df[['month', 'day']]
y = df['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestRegressor()
model.fit(X_train, y_train)
joblib.dump(model, "models/sales_model.pkl")
print("Model Trained & Saved")

