import plotly.graph_objects as go
import pandas as pd

userid  =  input("~enter your student id to check your performane")

df = pd.read_csv("data.csv")
student_df = df.loc[df['student_id']== userid]



print(student_df.groupby("level")["attempt"].mean())

fig  =  go.Figure(go.Bar(x=student_df.groupby("level")["attempt"].mean(),y = ['Level 1','Level 2','Level 3','Level 4'],orientation ="h"))


fig  =  go.Figure(go.Bar(x=df.groupby("level")["attempt"].mean(),y = ['Level 1','Level 2','Level 3','Level 4'],orientation ="h"))













