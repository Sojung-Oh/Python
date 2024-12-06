
from bs4 import BeautifulSoup
import requests

# #실습3. 환율 정보 크롤링 하기

html_url = "https://finance.naver.com/marketindex/"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, 'html.parser')
usd = soup.select_one("#exchangeList .usd .value")
print("USD: ", usd.text)

jpy = soup.select_one("#exchangeList .jpy .value")
print("JPY: ", jpy.text)

eur = soup.select_one("#exchangeList .eur .value")
print("EUR: ", eur.text)

cny = soup.select_one("#exchangeList .cny .value")
print("CNY: ", cny.text) #------------------------------실행 성공!

#실습4

# def stock(code):
#     html_url = f"https://finance.naver.com/item/main.naver?code={code}"
#     res = requests.get(html_url)
#     soup = BeautifulSoup(res.text, 'html.parser')

#     company = soup.select_one(" .wrap_company > h2 > a")
#     print("회사명: ", company.text.strip())

#     price = soup.select_one(" .today > .no_today .blind")
#     print("종가: ",price.text.strip())

#     aprice = soup.select(".today > .no_exday .blind")
#     print("전일대비: ", aprice[0].text.strip())


# #함수화시키기
# stock("035720")

