# add code for the last 10 days
import os
import templates
from chart import make_chart_for_day

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
  pngname = make_chart_for_day (date, total_score, max_score)
  all_lines [chart_line_index + 1] = f"![[{pngname}]]"
  return "\n".join(all_lines)


def add_md_2_day(date="25/01/02"):
  path = f"./{date}.md"
  md_data = edite_total_and_chart_2_day(templates.day_empty_data)
  update_file(path, md_data)

def update_md_day (date = "25/01/02"):
  path = f"./{date}.md"
  old_data = open (path, "r", encoding= "UTF-8")
  new_data = edite_total_and_chart_2_day (old_data.read(), date)
  old_data.close()
  update_file (path, new_data)

update_md_day ("25/01/05")