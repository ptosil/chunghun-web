
import requests, json
from datetime import datetime, timedelta

KEY = "00672036b41d4c5b9c44e53c64bd288f"
ATPT_OFCDC_SC_CODE = "J10"  # 경기도교육청
SD_SCHUL_CODE = "7010569"   # 충훈고등학교 코드

today = datetime.today()
start_date = today.strftime("%Y%m%d")
end_date = (today + timedelta(days=30)).strftime("%Y%m%d")  # 한 달치 일정

url = f"https://open.neis.go.kr/hub/SchoolSchedule?KEY={KEY}&Type=json&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}&SD_SCHUL_CODE={SD_SCHUL_CODE}&AA_YMD={start_date}"

res = requests.get(url)
data = res.json()

schedule_dict = {}

try:
    rows = data['SchoolSchedule'][1]['row']
    for item in rows:
        date = item['AA_YMD']
        content = item['EVENT_NM']
        schedule_dict[date] = content
    with open("calendar.json", "w", encoding="utf-8") as f:
        json.dump(schedule_dict, f, ensure_ascii=False, indent=2)
    print("✅ 학사일정 저장 완료!")
except Exception as e:
    print("❌ 학사일정 가져오기 실패:", e)
