import requests, json
from datetime import datetime

KEY = '00672036b41d4c5b9c44e53c64bd288f'
ATPT_OFCDC_SC_CODE = 'J10'
SD_SCHUL_CODE = '7530626'
today = datetime.today().strftime('%Y%m%d')

url = (
    f'https://open.neis.go.kr/hub/mealServiceDietInfo'
    f'?KEY={KEY}&Type=json&pIndex=1&pSize=100'
    f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
    f'&SD_SCHUL_CODE={SD_SCHUL_CODE}&MLSV_YMD={today}'
)

res = requests.get(url)
data = res.json()

try:
    meal = data['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
except:
    meal = '오늘 급식 정보가 없습니다.'

with open('lunch.json', 'w', encoding='utf-8') as f:
    json.dump({today: meal}, f, ensure_ascii=False, indent=2)

print("✅ lunch.json 자동 저장 완료")
