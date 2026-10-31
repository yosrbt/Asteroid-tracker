import matplotlib.pyplot as plt

def plot_top_sizes(df):
    plt.barh(df["name"], df["diameter_m"])
    plt.xlabel("Diamètre estimé (m)")
    plt.title("Top 10 des plus gros astéroïdes")
    plt.tight_layout()
    plt.show()

def plot_size_vs_distance(df):
    plt.scatter(df["distance_km"], df["diameter_m"], c=df["hazardous"])
    plt.xscale("log")
    plt.xlabel("Distance (km)")
    plt.ylabel("Diamètre (m)")
    plt.title("Taille vs distance")
    plt.show()
    