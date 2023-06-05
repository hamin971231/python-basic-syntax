# 코인시세정보 api url
# BTCUSDT
import requests 
from bs4 import BeautifulSoup
import json
url = "https://api.binance.com/api/v3/ticker/24hr"
response = requests.get(url)
data_json = json.loads(response.text)

# 키는 symbol : 'BTCUSDT', 'lastPrice' : 
# 출력 결과가 print(f'{} price는 {lastPrice}')

# for i in data_json :
#     if i['symbol']=='BTCUSDT' :
#         print(f"{i['symbol']} 코인의 가격은 {i['lastPrice']} 입니다.")
        # 값을 변수에 담아서 db에 저장해야함

# 코인시세 10초에 한번씩 db insert 
import mysql.connector
import time
try :
    connector = mysql.connector.connect(host='localhost',
                                        port='3306',
                                        user='root',
                                        password='1234',
                                        database='practice')
except mysql.connector.error as err :
    print(err)
while True :
    for i in data_json :
        if i['symbol']=='BTCUSDT' :
            cursor=connector.cursor()
            add_data='INSERT INTO coin_price (coin_name,last_price) values (%s,%s)'
            data=('BTCUSDT',i['lastPrice'])
            try :
                cursor.execute(add_data,data)
                connector.commit()
            except mysql.connector.error as err:
                print(err)
    time.sleep(10)
cursor.close()
connector.close()


# ## pip install mysql-connector-python
# ## mysql 파이썬 연동 라이브러리
# import mysql.connector
# try:
#     connector = mysql.connector.connect(
#         host='localhost',
#         port='3306',
#         user='root',
#         password='1234',database='practice')

#     # 커서객체는 데이터베이스에서 쿼리의 결과를 검석하고 순회하는데 사용되는 객체
#     cursor=connector.cursor()
# except  mysql.connector.error as err :
#     print(err)
# add_data = 'INSERT INTO author (name,email) values (%s,%s)' 
# data=("john",'hello2@naver.com')
# try:
#     cursor.execute(add_data,data)
#     connector.commit()
# except mysql.connector.error as err :
#     print(err)

cursor.close()
connector.close()

