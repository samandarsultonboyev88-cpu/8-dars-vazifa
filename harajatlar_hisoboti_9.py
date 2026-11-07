import csv

jami_xarajat = 0
xarajatlar_soni = 0
eng_katta_nom = ""
eng_katta_summa = 0

with open("expenses.csv", "r", encoding="utf-8") as f:
  reader = csv.DictReader(f)

  for row in reader:
    summa = int(row["summa"])
    jami_xarajat += summa
    xarajatlar_soni += 1

    if summa > eng_katta_summa:
      eng_katta_summa = summa
      eng_katta_nom = row["nom"]

print("Jami xarajat:", jami_xarajat)
print("Eng katta xarajat:", eng_katta_nom, "| Summasi:", eng_katta_summa)
print("Xarajatlar soni:", xarajatlar_soni)