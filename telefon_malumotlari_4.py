import json

with open("phone.json", "r", encoding="utf-8") as f:
  phone = json.load(f)

print("Modeli:", phone["model"], "| Eski narxi:", phone["narx"])

yangi_narx = int(input("Yangi narxni kiriting: "))
phone["narx"] = yangi_narx

with open("phone.json", "w", encoding="utf-8") as f:
  json.dump(phone, f, ensure_ascii=False, indent=4)

print("Modeli:", phone["model"], "| Yangi narxi:", phone["narx"])