# 🌠 Asteroid Tracker

Python app that fetches near-Earth asteroid data from the NASA NeoWs API,
cleans it with pandas and displays it in an interactive Streamlit dashboard.

## Features
- Fetches asteroids approaching Earth over 7 days
- Sorts by size and computes distances (km and Earth-Moon distances)
- Filters: potentially hazardous, minimum diameter
- Interactive Plotly charts

## Tech stack
Python, requests, pandas, Plotly, Streamlit

## Installation
1. Clone the repo
2. `python -m venv venv` and activate it
3. `pip install -r requirements.txt`
4. Get a key at https://api.nasa.gov and create a `.env` file:
   `NASA_API_KEY=your_key`
5. `streamlit run app.py`

## Project structure
- `fetch.py`: NASA API calls
- `process.py`: JSON to DataFrame
- `app.py`: Streamlit dashboard

## Screenshots
![Dashboard overview](images/dashboard1.png)
![Dashboard overview](images/dashboard2.png)

🔗 Live demo: https://asteroid-tracker-zzyxssrmpb7bdcwczpbxdq.streamlit.app/
