import json

with open("user.json", "r", encoding="utf-8") as f:
  data = json.load(f)

print(
    "Ismi:",
    data["ism"],
    "| Yoshi:",
    data["yosh"],
    "| Shahar:",
    data["shahar"],
)