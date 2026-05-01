import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

key = os.environ.get('VISUAL_CROSSING_API_KEY')
print(f"Key: [{key}]")
