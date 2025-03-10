**Cryptocurrency Data Fetching and Visualization**

**Overview**
This script fetches cryptocurrency data from the CoinMarketCap API, stores it in a CSV file, and visualizes key metrics using Seaborn and Matplotlib. The script runs multiple iterations to gather data at one-minute intervals and generates insights into cryptocurrency price changes over various timeframes.

**Features**
Fetches the latest cryptocurrency data from CoinMarketCap API.
Stores the retrieved data in a CSV file (crypto_data.csv).
Aggregates data for different timeframes (1h, 24h, 7d, 30d, 60d, 90d).
Generates a line plot for Bitcoin price trends over time.
Uses Seaborn for visualization of percentage changes across multiple cryptocurrencies.

**Dependencies**
The script requires the following Python libraries:
requests (for API calls)
json (for handling JSON responses)
pandas (for data processing and storage)
time (for periodic data fetching)
seaborn (for visualization)
matplotlib.pyplot (for plotting graphs)
os (for file handling)

**Installation**
Ensure you have Python installed, then install the required dependencies:
pip install requests pandas seaborn matplotlib

**Usage**
Replace API_KEY with your valid CoinMarketCap API key.
Run the script to start fetching and storing cryptocurrency data:
python script.py
The script will fetch data 10 times with a 60-second delay between each request.
Data is saved in crypto_data.csv and visualizations are generated at the end.

**Visualization**
A point plot of percentage changes for different timeframes.
A line plot showing Bitcoin price trends over time.

**Notes**
Ensure you have a valid API key for CoinMarketCap.
Avoid excessive API requests to prevent rate limiting.
The script appends data to crypto_data.csv, allowing long-term trend analysis.
