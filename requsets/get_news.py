import requests
from bs4 import BeautifulSoup

url = "https://www.itworld.co.kr/news"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

#가장 최신 페이지의 뉴스리스트을 가져오기
news_lists = soup.find_all("div",{"class":"news_list_"})

news = []

for news_list in news_lists:
    news_name = news_list.find("h4")["title"]
    news_link = "https://www.itworld.co.kr/" + news_list.find("a")["href"]
    latest_news = {"title":news_name, "link":news_link}
    news.append(latest_news)
print(news[0].get("title"))
