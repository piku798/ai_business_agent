import pandas as pd
import matplotlib.pyplot as plt
from utils import clean_data
#Read the dataset
df = pd.read_csv(r'C:\Users\nnaya\Desktop\ai_business_agent\data\retail_sales_dataset.csv')
print("First 5 rows of the dataset:")
print(df.head())
print(df.info())
print(df.describe())
# conveert date column 
df['Date'] = pd.to_datetime(df['Date'])

# monthely sales 
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()

monthly_sales.plot(title ="Monthly Sales trend")
plt.savefig(r'C:\Users\nnaya\Desktop\ai_business_agent\data\monthly_sales_trend.png')
plt.close()
df = clean_data(df)