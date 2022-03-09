
import pandas as pd
import json
import plotly
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go



start_date = '2021-01-01'
end_date =  '2021-12-31'
### get the counts into a list for each type 
orange_counts = [1,2,3,4,5,6,7,8,9,10,11,12]
apple_counts = [12,11,10,9,8,7,6,5,4,3,2,1]
### build a range of dates 
dates = pd.date_range(start_date, end_date, freq='MS')
fig = go.FigureWidget()
fig.update_layout(title="apple and orange counts")
## for each list of results add it to the graph 
fig.add_bar(x=dates, y= orange_counts, name = "monthly_orange_counts")
fig.add_bar(x=dates, y= apple_counts, name = "monthly_apple_counts")
##print(dates)
## add the dates to the graph 
fig.layout.xaxis.tickvals = pd.date_range(start_date, end_date, freq='MS')   
## make the ticks bold      
fig.layout.xaxis.tickformat = '%b'
# spit the graph out to a nice html file 
fig.write_html("simple_graph.html")



