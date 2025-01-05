import matplotlib.pyplot as plt

def make_chart_for_day (date, total_score, max_score):
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