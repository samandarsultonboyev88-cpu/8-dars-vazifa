import json

with open("product.json", "r", encoding="utf-8") as f:
  product = json.load(f)

umumiy_qiymat = product["narx"] * product["miqdor"]

print("Nomi:", product["nom"], "| Umumiy qiymati:", umumiy_qiymat)