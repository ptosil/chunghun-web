import requests, json
from datetime import datetime

KEY = "00672036b41d4c5b9c44e53c64bd288f"
ATPT_OFCDC_SC_CODE = "J10"
SD_SCHUL_CODE = "7530626"
GRADE = "3"
CLASS_NM = "7"

today = datetime.today().strftime("%Y%m%d")
url = (
    f"https://open.neis.go.kr/hub/hisTimetable"
    f"?KEY={KEY}&Type=json&pIndex=1&pSize=100"
    f"&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}"
    f"&SD_SCHUL_CODE={SD_SCHUL_CODE}"
    f"&GRADE={GRADE}&CLASS_NM={CLASS_NM}"
    f"&ALL_TI_YMD={today}"
)

print("⏳ 요청 URL:", url)

res = requests.get(url)
data = res.json()

print("📦 전체 JSON 구조:\n", json.dumps(data, indent=2, ensure_ascii=False))

timetable = {}

try:
    rows = data["hisTimetable"][1]["row"]
    for row in rows:
        period = row["PERIO"]
        subject = row["ITRT_CNTNT"]
        timetable[period] = subject

    with open("timetable.json", "w", encoding="utf-8") as f:
        json.dump(timetable, f, ensure_ascii=False, indent=2)
    print("✅ 시간표 저장 완료!")
except Exception as e:
    print("❌ 시간표 없음 또는 파싱 실패")
    print("에러 내용:", e)


