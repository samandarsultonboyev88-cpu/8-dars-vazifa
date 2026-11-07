import csv

with open("students.csv", "r", encoding="utf-8") as f:
  reader = csv.DictReader(f)

  for row in reader:
    print("Ismi:", row["ism"], "| Yoshi:", row["yosh"], "| Kursi:", row["kurs"])
    if int(row["yosh"]) > 20:
      print("--> 20 yoshdan katta:", row["ism"])