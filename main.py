import os
import requests
import time
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get your API key from environment variables
api_key = os.getenv("POLYGON_API_KEY")

# From Polygon.io
ticker = 'C:EURUSD'  # Note the ticker format for currency pairs
sma_url = f"https://api.polygon.io/v1/indicators/sma/{ticker}?timespan=day&adjusted=true&window=50&series_type=close&order=desc&apiKey={api_key}"

# Make the SMA API request
sma_response = requests.get(sma_url)

# Check if the request was successful
if sma_response.status_code == 200:
    sma_data = sma_response.json()
    # Process the SMA data as needed
    print("SMA Data:")
    print(sma_data)
else:
    print(f"SMA request failed with status code: {sma_response.status_code}")

# Countdown
countdown_time = 15  # seconds

for remaining_time in range(countdown_time, 0, -1):
    print(f"Continuing in {remaining_time} seconds...", end="\r")
    time.sleep(1)

print("\nCountdown completed. Continuing with the rest of the program.")
