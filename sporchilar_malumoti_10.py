import csv

eng_yuqori_ball = -1
eng_yuqori_sportchi = ""

with open("sportchilar.csv", "r", encoding="utf-8") as f:
  reader = csv.DictReader(f)

  for row in reader:
    ball = int(row["ball"])
    print(
        "Sportchi:",
        row["ism"],
        "| Sport turi:",
        row["sport"],
        "| Ball:",
        ball,
    )

    if ball > 80:
      print("--> 80 balldan yuqori:", row["ism"])

    if ball > eng_yuqori_ball:
      eng_yuqori_ball = ball
      eng_yuqori_sportchi = row["ism"]

print(
    "Eng yuqori ball olgan sportchi:",
    eng_yuqori_sportchi,
    "| Ball:",
    eng_yuqori_ball,
)