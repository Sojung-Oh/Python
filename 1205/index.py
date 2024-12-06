#리더님 동적 크롤링 실습 예시 코드


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#옵션 객체
options = Options()


#옵션 추가
options.add_argument("--start-maximized")
#options.add_argument("--headless")
options.add_argument("--incognito") #로그인하기 위해 시크릿 모드 옵션 켜기


options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe" 
#왜 나는 자동으로 크롬 드라이버가 다운이 안 될까... 결국 수동으로 다운 받고 직접 파일 경로를 지정해줬다.
service = Service("C:/Users/HOME/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

#실습 1번


# #웹사이트 지정 -나는 클릭이 안 먹혀서 로그인 페이지부터...
# driver.get("https://github.com/login")
# print(driver.title)
# print(driver.current_url)

# #이메일
# #emailadd = driver.find_element(By.ID, 'login_field') #id는 그 웹사이트 페이지에 하나뿐이므로 ID 적극 활용!
# driver.find_element(By.ID, 'login_field').send_keys("Sojung-Oh") #메서드를 계속 이어 붙이는 에서드 체인 방식!
# #emailadd.send_keys("Sojung-Oh")

# #password

# driver.find_element(By.ID, 'password').send_keys("dhthfl545400")
# #passwd = driver.find_element(By.XPATH, '//*[@id="password"]')
# #passwd.send_keys("dhthfl545400")

# driver.find_element(By.NAME, 'commit').click()
# #button = driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
# #button.click()

# #name = driver.find_element(By.XPATH, '')

# input("대기")

#===================================================================================================

#실습 2번 쇼핑몰 크롤링

# driver.get("https://www.11st.co.kr/")

# find = driver.find_element(By.XPATH, '//*[@id="tSearch"]/form/fieldset/input')
# find.send_keys("노트북")
# find.send_keys(Keys.ENTER)


# time.sleep(5)

# items = driver.find_elements(By.CSS_SELECTOR, ".c-search-list__item")

# for item in items:
#     name = item.find_element(By.CSS_SELECTOR, ".c-search-list__item > div .c-card-item__name > dd").text
#     price = item.find_element(By.CSS_SELECTOR, ".c-search-list__item > div .c-card-item__price > span").text
#     price = int(price.replace(',', ''))
#     if price > 500000:
#         print(f"상품명: {name}, 가격: {price}")
    # print(name)
    # print(price)

#================================================================================================================
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait  #이거 두 개는 같이 들어간다 생각하기

# EC 메서드
# EC.title_is("title") #현재 페이지 제목이 지정된 문자열과 일치할 때
# EC.title_contains("문자열") # 현재 페이지 제목에 문자열이 포함될 때
# EC.presence_of_element_located((By.ID, '아이디값')) # 값의 (태그=돔 요소)DOM이 존재할 때, 아이디는 예시일 뿐(화면 표시 안 되어도 됨) 
# EC.visibility_of_element_located((By.CSS_SELECTOR, "선택자")) # DOM이 존재할 때(화면에 표시)
# EC.presence_of_all_elements_located((By.CSS_SELECTOR, "선택자")) #DOM의 모든 요소가 존재할 때
# EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '선택자')) #DOM에 모든 요소가 존재할 때 (화면에 표시)
# EC.element_to_be_clickable((By.CSS_SELECTOR, '선택자')) #요소가 화면에 표시되고 클릭이 가능할 때
# EC.element_to_be_selected((By.CSS_SELECTOR, '선택자')) #요소가 선택된 상태가 될 때



#===================================================================================================
#실습3. 여행 사이트 크롤링 하기

from selenium.webdriver.support import expected_conditions as EC 

driver.get("https://www.agoda.com/ko-kr/")

time.sleep(3)

search = driver.find_element(By.ID, 'textInput')
search.click()
search.send_keys("도쿄")

# WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, 'textInput'))
# ) #10초는 최대 대기 시간

time.sleep(3)
search.send_keys(Keys.ESCAPE)

checkin = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "check-in-box"))
)

checkin.click()
#driver.find_element(By.ID, 'check-in-box').click()



#time.sleep(5)

#input("대기")

#리더님 코드 참고해서 수정하기

#클릭 가능한 상태가 된다면 클릭한다! 10초 넘어가면 오류 발생시키고, 10초 넘어가기 전에 클릭할 수 있게 되면 넘어가기
#집 가서 슬립 쓰던 거 다 웹드라이버 웨잇으로 바꿔보기!

driver.find_element(By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[2]/div[3]/div[1]/div[3]/div/div/div').click()
driver.find_element(By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[2]/div[3]/div[1]/div[7]/div/div/div').click()

driver.find_element(By.ID, 'occupancy-box').click()


#driver.find_element(By.XPATH, '//*[@id="Tabs-Container"]/button').click()



tab = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="Tabs-Container"]/button'))
)
tab.click()

time.sleep(7)


#마지막으로 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

hotels = WebDriverWait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.hotel-list-container h3'))
)

#hotels = driver.find_elements(By.CSS_SELECTOR, ".hotel-list-container h3")
price = driver.find_elements(By.CSS_SELECTOR, ".hotel-list-container .PropertyCardPrice__Value")

print(f"호텔명: {hotels[0].text}, 가격: {price[0].text}")

for hotel in hotels:
    print(hotel.text)

#============================================================================================
#실습4. 이미지 크롤링하기

# driver.get("https://www.google.co.kr/")

# time.sleep(3)

# search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
# search.click()
# search.send_keys("햄스터")
# search.send_keys(Keys.ENTER)
# time.sleep(2)
# #이미지 탭 들어가기
# driver.find_element(By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div').click()

# #스크롤 끝까지 내리기

# for _ in range(3):
#     driver.execute_script("window.scrollTo(0, document.body.scrollheight);")
#     images = driver.find_elements(By.CLASS_NAME, 'wIjY0d')

# i = 0

# for image in images[:30]:
#     i += 1
#     image.get_attribute("src")
#     with open(f"./1205/{i}.png", "wb")

# 리더님 예시

# import os
# import requests

# driver.get("https://www.google.co.kr/imghp")

# time.sleep(2)

# search = driver.find_element(By.ID, 'APjFqb')
# search.click()
# search.send_keys("햄스터")
# search.send_keys(Keys.ENTER)
# time.sleep(2)

# for i in range(5):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)


# images = driver.find_elements(By.CSS_SELECTOR, "img.YQ4gaf")

# os.makedirs("./1205/images", exist_ok=True) #폴더 생성, 존재하면 무시

# code = 1
# for image in images[:150]:
#     src = image.get_attribute("src")
#     #print(src)
#     if "https" in src:
#         res = requests.get(src)
#         print(res.content) # res.content 이미지, 동영상 값 반환
#         #res.status_code: 응답 코드
#         #res.headers: http 헤더의 정보 반환
#         #res.url: 최종 url 반환
#         with open(f"./1205/images/img_{code}.png", "wb") as file:
#             file.write(res.content)
#         code += 1




input("대기")



