# 아래 모듈은 외장 라이브러리 이므로, 별도 설치 필요
# 설치를 할 때 pip라는 패키지 tool 이용 파이선 설치시 동시에 설치됌 
# pip --version 헸을 때 버전정보가 안나오면
# 패스가 문제인데, path를 잡기보단 python 삭제후 재설치시 add path 옵션 체크함 .
# import requests 
# from bs4 import BeautifulSoup



# url = 'https://ko.wikipedia.org/wiki/%EC%95%84%EB%B0%94%ED%83%80:_%EB%AC%BC%EC%9D%98_%EA%B8%B8'

# 웹으로 주고받는 통신 프로토콜(약속)을 http통신이라고한다..
# http 통신을 하기 위해서는 http 통시규격에 맞게 request를 서버로 선달해야 한다
# request와 response는 header와 body로 이루어져있다.
# header={'User-Agent' : 'Mozilla/5.0'}

# response = requests.get(url, headers=header)
# html_reponse = BeautifulSoup(response.text, 'html.parser')

# for sup in html_reponse.find_all('sup') :
#     sup.decompose()
# print(html_reponse)
# 감독정보, 제작비정보
# tag 정보를 가지고 html_response에서 원하는 정보 추출

# director_info = html_reponse.select_one('table.infobox > tbody > tr:nth-of-type(3) > td').get_text()
# print(director_info)
# budget_info=html_reponse.select_one('table.infobox > tbody > tr:nth-of-type(16) > td').get_text()
# print(budget_info)


# 코인시세정보 api url
# BTCUSDT
# import json
# url = "https://api.binance.com/api/v3/ticker/24hr"

# response = requests.get(url)
# data_json = json.loads(response.text)
# print(data_json)
# 키는 symbol : 'BTCUSDT', 'lastPrice' : 
# 출력 결과가 print(f'{} price는 {lastPrice}')

# for i in data_json :
#     if i['symbol']=='BTCUSDT' :
#          print(f"{i['symbol']} 코인의 가격은 {i['lastPrice']} 입니다.")ㅂ

# csv파일 parsing
# import seaborn
# from matplotlib import pyplot
# import pandas


# file_path=r'C:\Users\조해민\tips.csv'
# csv_data=pandas.read_csv(file_path)

# # 성별에 따라 팁이 달라지는지
# agg :집계함수, mean :평균, std : 표준편차
# tib_by_gender = csv_data.groupby('gender')['tip'].agg(['mean','std']).reset_index()
# print(tib_by_gender)

# # 날짜에 따라 팁이 달라지는지
# tib_by_day = csv_data.groupby('day')['tip'].agg(['mean','std']).reset_index()

# seaborn.barplot(x='gender', y='mean',data=tib_by_gender,yerr=tib_by_gender['mean'],capsize=0.1)
# seaborn.despine() ## 테두리 없애주는 함수
# pyplot.title('average tip per gender')
# pyplot.xlabel('gender')
# pyplot.ylabel('average tip')
# pyplot.show()
seoul=["Jane", "Kim"]
answer=''
for i in range(len(seoul)) :
    if seoul[i]=='Kim' :
        print(seoul[i],i)
        