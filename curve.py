import plotly.figure_factory as pe
import pandas as pd
import csv

df = pd.read_csv("data.csv")

graph = pe.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist= False)
graph.show()