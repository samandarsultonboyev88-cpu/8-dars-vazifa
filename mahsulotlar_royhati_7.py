import csv

eng_qimmat_nom = ""
eng_qimmat_narx = 0

with open("products.csv", "r", encoding="utf-8") as f:
  reader = csv.DictReader(f)

  for row in reader:
    narx = int(row["narx"])
    miqdor = int(row["miqdor"])
    umumiy = narx * miqdor
    print("Nomi:", row["nom"], "| Umumiy qiymat:", umumiy)

    if narx > eng_qimmat_narx:
      eng_qimmat_narx = narx
      eng_qimmat_nom = row["nom"]

print("Eng qimmat mahsulot:", eng_qimmat_nom, "| Narxi:", eng_qimmat_narx)