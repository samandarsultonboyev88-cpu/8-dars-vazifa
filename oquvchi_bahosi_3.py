import json

with open("student.json", "r", encoding="utf-8") as f:
  student = json.load(f)

student["ball"] = 95

with open("student.json", "w", encoding="utf-8") as f:
  json.dump(student, f, ensure_ascii=False, indent=4)

print("O'quvchi:", student["ism"], "| Yangi ball:", student["ball"])