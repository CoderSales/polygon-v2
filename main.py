# From ChatGPT3.5
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Now you can access the API key using os.getenv("POLYGON_API_KEY")
api_key = os.getenv("POLYGON_API_KEY")

# From Polygon.io
ticker='AAPL'
start_date='2023-01-09'
end_date='2023-01-09'
url='https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}?apiKey={api_key}'
