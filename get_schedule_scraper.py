import requests
from bs4 import BeautifulSoup
import json

URL = "https://stu.goe.go.kr/sts_sci_sf01_001.do?schulCode=7010569&schulCrseScCode=4&schulKndScCode=04"
headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(URL, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

calendar_box = soup.select_one(".tbl_calendar")
events = {}

if calendar_box:
    tds = calendar_box.select("td")
    for td in tds:
        day = td.find("em")
        if not day:
            continue

        day_text = day.text.strip()
        desc = td.get_text().replace(day_text, "").strip().replace("\n", " ")

        if desc:
            events[day_text] = desc

    with open("calendar.json", "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)
    print("✅ 학사일정 저장 완료!")
else:
    print("❌ 학사일정 표를 찾을 수 없습니다.")
