import requests, json
from datetime import datetime

KEY = "00672036b41d4c5b9c44e53c64bd288f"
ATPT_OFCDC_SC_CODE = "J10"       # 경기도교육청
SD_SCHUL_CODE = "7530626"        # 충훈고등학교

today = datetime.today().strftime("%Y%m%d")

url = (
    f"https://open.neis.go.kr/hub/mealServiceDietInfo"
    f"?KEY={KEY}&Type=json&pIndex=1&pSize=100"
    f"&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}"
    f"&SD_SCHUL_CODE={SD_SCHUL_CODE}"
    f"&MLSV_YMD={today}"
)

res = requests.get(url)
data = res.json()

print("📡 요청 URL:", url)
print("📦 원본 응답 데이터:\n", json.dumps(data, indent=2, ensure_ascii=False))

try:
    meal = data["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
    meal = meal.replace("<br/>", "\n")
    
    with open("lunch.json", "w", encoding="utf-8") as f:
        json.dump({"date": today, "meal": meal}, f, ensure_ascii=False, indent=2)

    print("✅ lunch.json 저장 완료")
except Exception as e:
    print("❌ 오늘은 급식이 없거나 에러 발생")
    print("에러:", e)
