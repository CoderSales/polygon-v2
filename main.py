import os
import requests
import time
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
    print("Data:")
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")

# Countdown
countdown_time = 15  # seconds

for remaining_time in range(countdown_time, 0, -1):
    print(f"Continuing in {remaining_time} seconds...", end="\r")
    time.sleep(1)

print("\nCountdown completed. Continuing with the rest of the program.")
