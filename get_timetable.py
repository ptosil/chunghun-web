
import requests, json
from datetime import datetime

KEY = "00672036b41d4c5b9c44e53c64bd288f"
ATPT_OFCDC_SC_CODE = "J10"
SD_SCHUL_CODE = "7010569"
GRADE = "3"
CLASS_NM = "7"
SEMESTER = "1"
date = datetime.today().strftime("%Y%m%d")

url = (
    f"https://open.neis.go.kr/hub/hisTimetable?"
    f"KEY={KEY}&Type=json&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}"
    f"&SD_SCHUL_CODE={SD_SCHUL_CODE}&ALL_TI_YMD={date}"
    f"&GRADE={GRADE}&CLASS_NM={CLASS_NM}&SEM={SEMESTER}"
)

res = requests.get(url)
data = res.json()

timetable = {day: [] for day in ["월", "화", "수", "목", "금"]}

if "hisTimetable" in data:
    try:
        rows = data['hisTimetable'][1]['row']
        for item in rows:
            day = item['ALL_TI_YMD']
            weekday = datetime.strptime(day, "%Y%m%d").weekday()
            subject = item['ITRT_CNTNT']
            yoil = ["월", "화", "수", "목", "금"][weekday]
            if subject not in timetable[yoil]:
                timetable[yoil].append(subject)
    except Exception as e:
        print("⚠ 시간표 파싱 실패:", e)

with open("timetable.json", "w", encoding="utf-8") as f:
    json.dump(timetable, f, ensure_ascii=False, indent=2)

if any(timetable.values()):
    print("✅ 시간표 저장 완료!")
else:
    print("❌ 시간표 정보가 없습니다.")
