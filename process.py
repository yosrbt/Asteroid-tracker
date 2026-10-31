import pandas as pd

def to_dataframe(data):
    rows = []
    for day, objects in data["near_earth_objects"].items():
        for o in objects:
            approach = o["close_approach_data"][0]
            rows.append({
                "name": o["name"],
                "date": day,
                "diameter_m": o["estimated_diameter"]["meters"]["estimated_diameter_max"],
                "distance_km": float(approach["miss_distance"]["kilometers"]),
                "speed_kmh": float(approach["relative_velocity"]["kilometers_per_hour"]),
                "hazardous": o["is_potentially_hazardous_asteroid"],
            })
    df = pd.DataFrame(rows)
    df["distance_lunar"] = df["distance_km"] / 384_400  # distance en Terre-Lune
    return df

def top_biggest(df, n=10):
    return df.sort_values("diameter_m", ascending=False).head(n)