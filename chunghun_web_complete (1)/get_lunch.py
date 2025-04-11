import requests, json
from datetime import datetime

KEY = "00672036b41d4c5b9c44e53c64bd288f"
ATPT_OFCDC_SC_CODE = "J10"
SD_SCHUL_CODE = "7010569"
today = datetime.today().strftime("%Y%m%d")

url = f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY={KEY}&Type=json&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}&SD_SCHUL_CODE={SD_SCHUL_CODE}&MLSV_YMD={today}"
res = requests.get(url)
data = res.json()

try:
  meal = data['mealServiceDietInfo'][1]['row'][0]['DDISH_NM'].replace("<br/>", "\n")
  with open("lunch.json", "w", encoding="utf-8") as f:
    json.dump({"date": today, "meal": meal}, f, ensure_ascii=False, indent=2)
  print("✅ 급식 저장 완료!")
except:
  print("❌ 오늘은 급식이 없습니다.")
