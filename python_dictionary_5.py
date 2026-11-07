import json

talaba = {"ism": "Sardor", "yosh": 20, "kurs": 2}

json_matn = json.dumps(talaba, ensure_ascii=False)
print("JSON matn:", json_matn)

qayta_dict = json.loads(json_matn)
print("Ismi:", qayta_dict["ism"], "| Kursi:", qayta_dict["kurs"])