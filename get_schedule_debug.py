import requests, json
from datetime import datetime, timedelta

KEY = "00672036b41d4c5b9c44e53c64bd288f"
ATPT_OFCDC_SC_CODE = "J10"
SD_SCHUL_CODE = "7010569"

start_date = datetime(2025, 4, 1)
end_date = datetime(2025, 9, 30)

events = {}

while start_date <= end_date:
    ymd = start_date.strftime("%Y%m%d")
    url = (
        f"https://open.neis.go.kr/hub/SchoolSchedule?KEY={KEY}"
        f"&Type=json&pIndex=1&pSize=100"
        f"&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}"
        f"&SD_SCHUL_CODE={SD_SCHUL_CODE}"
        f"&AA_YMD={ymd}"
    )

    print(f"📅 요청 중: {ymd}")
    res = requests.get(url)
    data = res.json()
    print(json.dumps(data, indent=2, ensure_ascii=False))  # << 전체 응답 출력

    try:
        rows = data["SchoolSchedule"][1]["row"]
        for row in rows:
            date = row["AA_YMD"]
            content = row["EVENT_NM"]
            if "고사" in content or "학" in content or "날" in content or "휴업일" in content:
                events[date] = content
    except:
        print("❌ 해당 날짜 일정 없음")

    start_date += timedelta(days=1)

with open("calendar.json", "w", encoding="utf-8") as f:
    json.dump(events, f, ensure_ascii=False, indent=2)
print("✅ calendar.json 저장 완료")
