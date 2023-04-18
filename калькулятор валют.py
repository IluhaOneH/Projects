import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *

WIDTH = 300
HEIGHT = 250
result = 0
w = tk.Tk()
response = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&sxsrf=APwXEdethyQYnGDc-AeQwMf9P1hoP2Enmg%3A1681760165850&ei=pZ89ZJWKM-jixc8Pip2_yAs&ved=0ahUKEwjV8KDq1LH-AhVocfEDHYrOD7kQ4dUDCA8&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIKCAAQgAQQFBCHAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoPCAAQigUQ6gIQtAIQQxgBOgQIIxAnOgsILhCABBDHARDRAzoJCAAQgAQQChAqOgcIABCABBAKOgcILhCABBAKOggILhCABBDUAjoJCAAQgAQQChABOgcIABCKBRBDOgUILhCABDoKCC4QigUQ1AIQQ0oECEEYAFCVEFj9Y2CFaWgFcAF4AIABdYgB1gqSAQQxOC4xmAEAoAEBsAEUwAEB2gEGCAEQARgB&sclient=gws-wiz-serp'
user = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
page = requests.get(response, headers = user)

soup = BeautifulSoup(page.content, 'html.parser')
search = soup.find_all("span", {"class": "DFlfde SwHCTb", "data-precision": "2"})
src = search[0]
print(src.text)

def cancel():
    entry1_e.delete("0", END)
    entry2_e.delete("0", END)

def ok():
    result = float(entry1_e.get()) / float(src.text.replace(",", "."))
    if entry2_e != "":
        entry2_e.delete("0", END)
        entry2_e.insert(0, round(result, 2))
    else:
        entry2_e.insert(0, round(result, 2))

w.title('Калькулятор валют')
w.geometry('%dx%d' % (WIDTH, HEIGHT))
w.resizable(True, True)

start = tk.Label(w, text="КАЛЬКУЛЯТОР ВАЛЮТ", font=('Comic Sans MS', 14))
start.pack()

course = tk.Label(w, text = "Текущий курс: "+ src.text.replace(",", "."), font=('Comic Sans MS', 10))
course.pack(anchor = NW, padx = 85, pady = 5)

entry1_e = tk.Entry(w)
entry1_e.insert(0, "HRIVNA")
entry1_e.pack(anchor=NW, padx = 100, pady = 10)


entry2_e = tk.Entry(w)
entry2_e.insert(0, "USD")
entry2_e.pack(anchor=NW, padx = 100, pady = 10)



b_ok = tk.Button(w, text="Convert", command=ok)
b_ok.pack(anchor=NW, padx = 90, pady = 14, side = LEFT)

b_cancel = tk.Button(w, text="Clear", command=cancel)
b_cancel.pack(anchor=NW, pady = 14)



w.mainloop()

