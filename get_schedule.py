
import requests, json

KEY = "00672036b41d4c5b9c44e53c64bd288f"
ATPT_OFCDC_SC_CODE = "J10"
SD_SCHUL_CODE = "7010569"

start_date = "20250401"
end_date = "20250930"

url = (
    f"https://open.neis.go.kr/hub/SchoolSchedule?"
    f"KEY={KEY}&Type=json&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}"
    f"&SD_SCHUL_CODE={SD_SCHUL_CODE}&AA_FROM_YMD={start_date}&AA_TO_YMD={end_date}"
)

res = requests.get(url)
data = res.json()

schedule = {}

if "SchoolSchedule" in data:
    try:
        rows = data['SchoolSchedule'][1]['row']
        for item in rows:
            date = item['AA_YMD']
            event = item['EVENT_NM']
            schedule[date] = event
    except Exception as e:
        print("⚠ 일정 파싱 실패:", e)

with open("calendar.json", "w", encoding="utf-8") as f:
    json.dump(schedule, f, ensure_ascii=False, indent=2)

if schedule:
    print("✅ 학사일정 저장 완료!")
else:
    print("❌ 학사일정이 없습니다.")
