from datetime import date
from fetch import get_asteroids
from process import to_dataframe, top_biggest
from charts import plot_top_sizes, plot_size_vs_distance

df = to_dataframe(get_asteroids(date.today()))
plot_top_sizes(top_biggest(df))
plot_size_vs_distance(df)