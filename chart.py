

def make_chart_for_day_mat (date, total_score, max_score):
  import matplotlib.pyplot as plt
  plt.style.use ("ggplot")
  plt.title (f"The result of the day : {date}")
  plt.pie ([total_score, max_score - total_score], 
          (0.1, 0), 
          ["Tasks done", "Task not done"], 
          ["#ADD8E6", "red"],
          autopct= "%1.1f%%",
          pctdistance= 0.8,
          shadow= True)
  plt.rcParams ["font.family"] = "Arial"
  name = f"DayChart_{date.replace ('/', '-')}.png"
  plt.savefig (f"./all_charts/{name}")
  return name

import plotly.graph_objects as go

def make_chart_for_day_ly (date, total_score, max_score):
    scores = [total_score, max_score - total_score]
    labels = ["Tasks done", "Tasks not done"]
    colors = ["#ADD8E6", "red"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=scores,
                pull=[0.1, 0],
                marker=dict(colors=colors),
                textinfo="percent+label",
            )
        ]
    )

    fig.update_layout(
        title_text=f"The result of the day : {date}",
        font=dict(family="Arial", size=14),
        showlegend=True,
    )

    name = f"DayChart_{date.replace('/', '-')}.png"
    fig.write_image(f"./all_charts/{name}") 
    return name
