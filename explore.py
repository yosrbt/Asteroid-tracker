import json
from datetime import date
from fetch import get_asteroids

data = get_asteroids(date.today())

print("Total :", data["element_count"])
print("Jours :", list(data["near_earth_objects"].keys()))

first_day = next(iter(data["near_earth_objects"].values()))
print(json.dumps(first_day[0], indent=2)[:1500])