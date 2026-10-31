import streamlit as st
import plotly.express as px
from datetime import date

from fetch import get_asteroids
from process import to_dataframe

st.set_page_config(page_title="Asteroid Tracker", page_icon="🌠", layout="wide")
st.title("🌠 Asteroid Tracker")
st.caption("Données : NASA NeoWs (Near Earth Object Web Service)")

# --- Chargement des données ---
start = st.date_input("Date de début (7 jours affichés)", date.today())

@st.cache_data(ttl=3600)
def load(d):
    return to_dataframe(get_asteroids(d))

try:
    df = load(start)
except Exception as e:
    st.error(f"Impossible de récupérer les données : {e}")
    st.stop()

if df.empty:
    st.warning("Aucun astéroïde trouvé pour cette période.")
    st.stop()

# --- Filtres ---
st.sidebar.header("Filtres")
only_hazard = st.sidebar.checkbox("Seulement les potentiellement dangereux")
max_size = max(1, int(df["diameter_m"].max()))
min_size = st.sidebar.slider("Diamètre minimum (m)", 0, max_size, 0)

if only_hazard:
    df = df[df["hazardous"]]
df = df[df["diameter_m"] >= min_size]

if df.empty:
    st.info("Aucun résultat avec ces filtres.")
    st.stop()

# --- Métriques ---
col1, col2, col3 = st.columns(3)
col1.metric("Astéroïdes", len(df))
col2.metric("Plus gros (m)", f"{df['diameter_m'].max():.0f}")
col3.metric("Plus proche (km)", f"{df['distance_km'].min():,.0f}")

# --- Graphiques ---
left, right = st.columns(2)

with left:
    st.subheader("Taille vs distance")
    fig1 = px.scatter(df, x="distance_km", y="diameter_m",
                      color="hazardous", hover_name="name",
                      size="speed_kmh", log_x=True)
    st.plotly_chart(fig1, use_container_width=True)

with right:
    st.subheader("Top 10 des plus gros")
    top = df.sort_values("diameter_m", ascending=False).head(10)
    fig2 = px.bar(top, x="diameter_m", y="name", orientation="h")
    fig2.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Vitesse des astéroïdes par jour")
fig3 = px.box(df, x="date", y="speed_kmh", color="hazardous")
st.plotly_chart(fig3, use_container_width=True)
# --- Tableau ---
st.subheader("Données")
st.dataframe(df.sort_values("diameter_m", ascending=False),
             use_container_width=True)