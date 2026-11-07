import csv

yangi_ism = input("Ismni kiriting: ")
yangi_yosh = input("Yoshni kiriting: ")
yangi_kurs = input("Kursni kiriting: ")

with open("students.csv", "a", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  writer.writerow([yangi_ism, yangi_yosh, yangi_kurs])

print("Yangi o'quvchi qo'shildi! Fayldagi barcha o'quvchilar:")
with open("students.csv", "r", encoding="utf-8") as f:
  reader = csv.reader(f)
  for row in reader:
    print("Ma'lumot:", row)