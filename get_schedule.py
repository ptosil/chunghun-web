import requests, json
from datetime import datetime, timedelta

KEY = "00672036b41d4c5b9c44e53c64bd288f"
ATPT_OFCDC_SC_CODE = "J10"  # 경기도교육청
SD_SCHUL_CODE = "7530626"   # 충훈고등학교

start_date = datetime.strptime("20250401", "%Y%m%d")
end_date = datetime.strptime("20250930", "%Y%m%d")

events = {}

print("🔄 학사일정 가져오는 중...")

while start_date <= end_date:
    ymd = start_date.strftime("%Y%m%d")
    url = (
        f"https://open.neis.go.kr/hub/SchoolSchedule"
        f"?KEY={KEY}&Type=json&pIndex=1&pSize=100"
        f"&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}"
        f"&SD_SCHUL_CODE={SD_SCHUL_CODE}"
        f"&AA_YMD={ymd}"
    )

    res = requests.get(url)
    data = res.json()

    try:
        rows = data["SchoolSchedule"][1]["row"]
        for row in rows:
            date = row["AA_YMD"]
            content = row["EVENT_NM"]
            if "고사" in content or "학" in content or "날" in content or "휴업일" in content:
                events[date] = content
        print(f"✅ {ymd} 일정 추가됨")
    except Exception:
        print(f"❌ {ymd} 해당 날짜 일정 없음")

    start_date += timedelta(days=1)

with open("calendar.json", "w", encoding="utf-8") as f:
    json.dump(events, f, ensure_ascii=False, indent=2)

print("✅ calendar.json 저장 완료")
