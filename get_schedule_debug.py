
import requests, json
from datetime import datetime

KEY = "00672036b41d4c5b9c44e53c64bd288f"
ATPT_OFCDC_SC_CODE = "J10"  # 경기도교육청
SD_SCHUL_CODE = "7010569"   # 충훈고등학교 코드
today = datetime.today().strftime("%Y%m%d")

url = f"https://open.neis.go.kr/hub/SchoolSchedule?KEY={KEY}&Type=json&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}&SD_SCHUL_CODE={SD_SCHUL_CODE}&AA_YMD={today}"

res = requests.get(url)
data = res.json()

print("📦 NEIS 응답 전체 JSON 구조 출력:")
print(json.dumps(data, indent=2, ensure_ascii=False))
