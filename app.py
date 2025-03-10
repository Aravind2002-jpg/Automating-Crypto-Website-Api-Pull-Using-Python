import requests
import json
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt
import os

API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
API_KEY = '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509'  
PARAMETERS = {
    'start': '1',
    'limit': '15',
    'convert': 'USD'
}
HEADERS = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}
CSV_FILE = 'crypto_data.csv'
def fetch_crypto_data():

    try:
        response = requests.get(API_URL, headers=HEADERS, params=PARAMETERS)
        response.raise_for_status()
        data = response.json()
        df = pd.json_normalize(data['data'])
        df['timestamp'] = pd.Timestamp.now()
        if not os.path.exists(CSV_FILE):
            df.to_csv(CSV_FILE, index=False)
        else:
            df.to_csv(CSV_FILE, mode='a', header=False, index=False)
        print("Data successfully fetched and stored.")
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")


for i in range(10):
    fetch_crypto_data()
    print(f"Iteration {i+1} completed.")
    time.sleep(60)  

#Should run the graph code  after the csv file is generated

df = pd.read_csv('crypto_data.csv')
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_grouped = df.groupby('name', sort=False)[[
    'quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d',
    'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d'
]].mean()

df_melted = df_grouped.stack().reset_index()
df_melted.columns = ['name', 'percent_change', 'values']
df_melted['percent_change'] = df_melted['percent_change'].replace({
    'quote.USD.percent_change_24h': '24h',
    'quote.USD.percent_change_7d': '7d',
    'quote.USD.percent_change_30d': '30d',
    'quote.USD.percent_change_60d': '60d',
    'quote.USD.percent_change_90d': '90d'
})

df_bitcoin = df[df['name'] == 'Bitcoin'][['timestamp', 'quote.USD.price']]
g = sns.catplot(x='percent_change', y='values', hue='name', data=df_melted, kind='point')
sns.lineplot(x='timestamp', y='quote.USD.price', data=df_bitcoin)
plt.xticks(rotation=45)
plt.title("Bitcoin Price Over Time")
plt.xlabel("Time")
plt.ylabel("Price (USD)")
plt.show()
