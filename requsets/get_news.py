import requests
import time
import csv
from bs4 import BeautifulSoup
import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Latest IT-issue"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS

url = "https://www.itworld.co.kr/news"
res = requests.get(url)
res.raise_for_status()

filename = "IT-issue.csv"
f=open(filename, "w", encoding="utf8", newline="")
writer = csv.writer(f)

soup = BeautifulSoup(res.text,"lxml")

#가장 최신 페이지의 뉴스리스트을 가져오기
news_lists = soup.find_all("div",{"class":"news_list_"})

#각각의 뉴스를 객체로 만들어 list에 저장
article=""
for news_list in news_lists:
    news_name = news_list.find("h4")["title"]
    news_link = "https://www.itworld.co.kr/" + news_list.find("a")["href"]
    news = [news_name, news_link]
    writer.writerow(news)
    article = article + "\n" + news_name+" "+news_link
    msg.set_content(article)

#이메일보내기
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)