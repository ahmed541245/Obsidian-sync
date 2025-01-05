# when this python file run it must add the code for the last day md files, the last monthe md files, last year md files

# add code for the last 10 days
import os
import templates


def loop_folder(folder_path, func):
  for root, dirs, files in os.walk(folder_path):
    for file in files:
      func(root, file)


def update_file(file_path, new_data):
  with open(file_path, "w", encoding="UTF-8") as f:
    f.write(new_data)


def edite_total_and_chart_2_day(md_data: str):
  totalpoints_line_index, chart_line_index = 2, 3
  all_lines = md_data.split("\n")
  max_score = 0
  total_score = 0
  line_index = chart_line_index + 1
  lines = all_lines[chart_line_index + 1:]
  heading_indexes = []
  linee_index = 4
  for linee in lines :
    if linee [0] == "#":
      heading_indexes.append (linee_index)
    linee_index += 1
  for line_index in heading_indexes:
    line = all_lines [line_index]
    if line[0] == "#":
      heading_parts = line.split(":")
      if len(heading_parts) > 1:
        score = int(heading_parts[-1])
      for line2 in lines[line_index:]:
        if line2[0:5] in ["- [ ]", "- [ ] ", "- [ "]:
          task_parts = line2.split(":")
          task_score = 1
          if len(task_parts) > 1 :
            task_score = int (task_parts[-1])
          else:
            if len(heading_parts) > 1:
              task_score = score
            else : task_score = 1
          max_score += task_score
          if "x" in [line2[3], line2[4], line2[2]]:
            total_score += int (task_score)
          print (f"heading : {line}   task : {line2}  score : {task_score}")
        elif "#" in line2[0:2]:
          break
    line_index += 1

  all_lines[
      totalpoints_line_index] = f"> Total points : {total_score}/{max_score}"
  unicode = '\u00A0'
  all_lines[
      chart_line_index] = f"> Chart : [{'='*total_score}{unicode*(max_score-total_score)}]"
  return "\n".join(all_lines)


def add_md_2_day(date="25/01/02"):
  path = f"./{date}.md"
  md_data = edite_total_and_chart_2_day(templates.day_empty_data)
  update_file(path, md_data)


add_md_2_day("25/01/02")
