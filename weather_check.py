import requests
import datetime
from bs4 import BeautifulSoup
import sqlite3

connection = sqlite3.connect("weath.sq3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS wea (town TEXT, date TEXT, time TEXT, temp TEXT);")
connection.commit()

link = "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BE%D1%81%D0%BB%D0%BE"
user = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
page = requests.get(link, headers=user)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, features="html.parser")
    temp_list = soup.find_all("div", {"class": "lSide"})
    temp = temp_list[0].find("p", {"class": "today-temp"})
    print(temp.text)
    cur.execute(f"INSERT INTO wea VALUES('Осло','{datetime.datetime.today().date()}','{datetime.datetime.today().time()}','{temp.text}')")
    connection.commit()
    connection.close()

