import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Now you can access the API key using os.getenv("POLYGON_API_KEY")
api_key = os.getenv("POLYGON_API_KEY")
