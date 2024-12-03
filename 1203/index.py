#웹스크래핑

from bs4 import BeautifulSoup
import requests


# html_str = """
# <html>
#     <body>
#         <div id = "contact">
#             <ul class = "industry">
#                 <li>인공지능</li>
#                 <li>빅데이터</li>
#                 <li>신재생에너지</li>

#             </ul>
#             <ul class = "comlang">
#                 <li>Python</li>
#                 <li>C++</li>
#                 <li>Javascript</li>

#             </ul>

#         </div>

#     </body>
# </html>
# """

# soup = BeautifulSoup(html_str, "html.parser")
# #print(soup)
# #print(soup.li.text)
# first_ul = soup.find("ul") #첫번째로 만나는 일치하는 태그 가져오기
# print(first_ul)
# print(first_ul.text) #태그 안에 있는 것은 텍스트! 태그 없이 텍스트 출력

# all_ul = soup.find_all('ul')
# print(all_ul[1])
# print(all_ul[1].text)

# class_ul = soup.find('ul', attrs = {'class': "comlang"})
# print(class_ul) # .find 명령어를 이용해서 쓰는 법
# print(class_ul.text)

# first_ul = soup.select_one("ul.industry") #일치 선택자 참고
# print(first_ul)
# print(first_ul.text)

#all_ul = soup.select("div > ul")
# all_ul = soup.select("#content > ul")
# print(all_ul)

# html_url = "https://www.seoul.go.kr/main/index.jsp"
# res = requests.get(html_url)
# #print(res)
# #print(res.text)
# soup = BeautifulSoup(res.text, 'html.parser')
# #print(soup) #텍스트로 오던 아까와 달리 객체로 들어옴
# all_nav = soup.select("nav > ul > li > a")
# #print(all_nav[1].text)
# for i in all_nav:
#     print(i.text)

#실습1. 국립중앙박물관 관람정보

# htmlurl = "https://www.museum.go.kr/site/main/home"
# res2 = requests.get(htmlurl)
# soup2 = BeautifulSoup(res2.text, 'html.parser')
# #print(soup2) 
# display_content = soup2.select("div.main > div.main-container > div.main-section-1")
# for i in display_content:
#     print(i.text)
# #print(display_content[1].text)

#리더님 예시

# htmlurl = "https://www.museum.go.kr/site/main/home"
# res2 = requests.get(htmlurl)
# soup2 = BeautifulSoup(res2.text, 'html.parser')
#print(soup2) 
#display_content = soup2.select("ul.main-info-area > li")
# infos = soup2.select("ul.main-info-area > li")
# # for i in infos:
# #     print(i.text)

# #관람 시간

# times = soup2.select(".info-time > ul > li")
# print(times)
# for i in times:
#     print("이용시간: ", i.text.strip())

# print()
# #관람료

# pay = soup2.select(".info-admission > ul > li") #배열로 나타남
# #print(pay)
# for i in pay:
#     print("관람료: ", i.text.strip())

#KBS 뉴스


# #html_url = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8117340"
# html_url = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8118240" #url 다른 기사 가져와도 같은 코드로 크롤링 가능!
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')
# title = soup.select_one(".headline-title")
# print("제목: ", title.text)

# print()

# contents = soup.select_one(".detail-body") #동적으로 하는 거라 앵커 리포트로 접근 불가
# print("내용: ", contents.text.strip())

# with open("news.txt", "w", encoding = "utf-8") as file:
#     file.write(contents.text.strip())

#실습2. 전자 신문 메인 기사 크롤링

# html_url = "https://www.donga.com/news/Society/article/all/20241203/130559522/1"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')

# title = soup.select_one(" .view_head > div.inner > section.head_group > h1")
# print("제목: ", title.text)
# print()
# issue_date = soup.select_one("ul.news_info > li > button")
# print("업데이트 날짜: ",issue_date.text.strip())
# print()
# article = soup.select_one("div.main_view > section.news_view")
# print("기사본문: ", article.text.strip())


#명언 사이트 크롤링 하기
# html_url = "https://quotes.toscrape.com/"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')
# quote = soup.select(".quote > .text")
# print(len(quote))

# # for i in quote:
# #     print(i.text.strip())

# text = [i.text.strip() for i in quote]
# print(text)

# speak = soup.select(".author")
# author = [i.text.strip() for i in speak]
# print(author)

# zipped = list(zip(text, author))
# print(zipped)

# for text, speak in zipped:
#     print(f"말한사람: {speak} \n내용: {text}")
#     print()

#실습3. 환율 정보 크롤링 하기

# html_url = "https://finance.naver.com/marketindex/"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')
# usd = soup.select_one("a.head.usd > div.head_info.point_dn > span")
# print("USD: ", usd.text)

# jpy = soup.select_one("a.head.jpy > div.head_info.point_dn > span")
# print("JPY: ", jpy.text)

# eur = soup.select_one("a.head.eur > div.head_info.point_dn > span")
# print("EUR: ", eur.text)

# cny = soup.select_one("a.head.cny > div.head_info.point_dn > span")
# print("CNY: ", cny.text)

#실습4. 주식 정보 크롤링 하기

html_url = "https://finance.naver.com/item/main.naver?code=035420"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, 'html.parser')
rate = soup.select_one("div.rate_info")
print(rate.text.strip())