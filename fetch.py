# fetch.py
import os
import sys
from pathlib import Path
from datetime import date, timedelta

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
URL = "https://api.nasa.gov/neo/rest/v1/feed"

def get_asteroids(start: date, days: int = 7):
    end = start + timedelta(days=days - 1)
    params = {"start_date": start.isoformat(),
              "end_date": end.isoformat(),
              "api_key": API_KEY}
    r = requests.get(URL, params=params, timeout=15)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    data = get_asteroids(date.today())
    print(data["element_count"], "astéroïdes trouvés")