	# add code for the last 10 days
import os
import templates
from chart import *

def loop_folder(folder_path, func):
  for root, dirs, files in os.walk(folder_path):
    for file in files:
      func(root, file)


def update_file(file_path, new_data):
  with open(file_path, "w", encoding="UTF-8") as f:
    f.write(new_data)


def edite_total_and_chart_2_day(md_data: str, date):
  totalpoints_line_index, chart_line_index = 2, 3
  all_lines = md_data.split("\n")
  max_score = 0
  total_score = 0
  # line_index = chart_line_index + 1
  # lines = all_lines[chart_line_index + 1:]
  heading_indexes = []
  linee_index = 0
  for linee in all_lines :
    if linee [0] == "#" and all_lines [linee_index +1][0] != ">":
      heading_indexes.append (linee_index)
    linee_index += 1
  for line_index in heading_indexes:
    line = all_lines [line_index]
    if line[0] == "#" :
      heading_parts = line.split(":")
      if len(heading_parts) > 1:
        score = int(heading_parts[-1])
      for line2 in all_lines[line_index + 1:]:
        # if all_lines.index (line2) >= heading_indexes[heading_indexes.index(line_index)] :
        #   break
        if line2[0:3] in ["- [", "-[ "]:
          task_parts = line2.split(":")
          task_score = 1
          if len(task_parts) > 1 : # check if the task score was detected
            task_score = int (task_parts[-1])
          else:
            if len(heading_parts) > 1: # check if the heading was detected
              task_score = score
            else : task_score = 1 # if nither, make it one
          max_score += task_score
          if "x" in [line2[3], line2[4], line2[2]]:
            total_score += int (task_score)
        elif "#" in line2[0:2]:
          break
    line_index += 1

  all_lines[totalpoints_line_index] = f"> Total points : {total_score}/{max_score}"
  unicode = '\u00A0'
  all_lines[
      chart_line_index] = f"> Chart : [{'='*total_score}{unicode*(max_score-total_score)}]"
  try :
    pngname = make_chart_for_day_mat (date, total_score, max_score)
  except :
    pngname = make_chart_for_day_ly (date, total_score, max_score)
  all_lines [chart_line_index + 1] = f"![[{pngname}]]"
  return "\n".join(all_lines)


def add_md_2_day(date="25/01/02"):
  path = f"./{date}.md"
  md_data = edite_total_and_chart_2_day(templates.day_empty_data, date)
  update_file(path, md_data)

def update_md_day (date = "25/01/02"):
  path = f"./{date}.md"
  old_data = open (path, "r", encoding= "UTF-8")
  new_data = edite_total_and_chart_2_day (old_data.read(), date)
  old_data.close()
  update_file (path, new_data)

print ("if you wanna close the app, pls type 'e' in any input\n")
while True :
  file_date = input ("Enter the date of the file you want to manage, or l for the last or a for all (YY/MM/DD, a, l) : ")
  if file_date == "e":
    break
  elif file_date in ["l", "a"]:
    folder_path = "./25"
    folders = sorted(os.listdir(folder_path))
    if file_date == "l":
      last_month = folders[-2]
      last_month_path = os.path.join (folder_path, last_month)
      days = sorted([f for f in os.listdir(last_month_path) if os.path.isfile(os.path.join(last_month_path, f))])
      last_day_date = "/".join(os.path.join (last_month_path, days[-2]).__str__().split("/")[-3:]).split(".")[0]

      date = last_day_date
  else :
    if os.path.isfile ("./"+file_date):
      date = file_date
    else :
      print ("your input is incorrect or this day date is not exit pls retry again")
      continue
  add_or_update = input ("What do you want, add md to file or update file (a, u) : ")
  if add_or_update == "e":
    break
  elif add_or_update == "a":
    add_md_2_day (date)
  elif add_or_update == "u":
    update_md_day(date)
  else :
    print ("your input is shit pls try again")

