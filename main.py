import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get your API key from environment variables
api_key = os.getenv("POLYGON_API_KEY")

# From Polygon.io
ticker = 'AAPL'
start_date = '2023-01-09'
end_date = '2023-01-09'

# Construct the complete URL with formatted strings
url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}?apiKey={api_key}"

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Process the data as needed
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
