import pandas as pd 
import plotly.express as px 
df = pd.read_csv("main.csv")

GRE_Score = df["GRE Score"].tolist() 
Chances_of_admit = df["Chance of Admit "].tolist() 


import numpy as np
GRE_Score_array = np.array(GRE_Score)
Chance_of_Admit_array = np.array(Chances_of_admit)

#slope and interscept
m, c = np.polyfit(GRE_Score_array,Chance_of_Admit_array,1)

y = []

for x in GRE_Score:
  yvalue = m*x+c
  y.append(yvalue)
fig = px.scatter(x=GRE_Score, y=Chances_of_admit) 
fig.update_layout(shapes = [
    dict(
        type = 'line',
         y0 = min(y), y1 = max(y),
         x0 = min(GRE_Score), x1 = max(GRE_Score)
    )
])
fig.show()