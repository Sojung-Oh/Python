# # selenium

# # from selenium import webdriver

# # driver = webdriver.Chrome()
# # driver.get("https://www.naver.com/")
# # print(driver.title)


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.microsoft import EdgeChromiumDriverManager
# # from selenium.webdriver.edge.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import time

# #옵션 객체
# options = Options()
# #옵션 추가
# options.add_argument("--start-maximized")
# #options.add_argument("--headless")
# options.add_argument("--incognito")

# options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe" 
# #왜 나는 자동으로 크롬 드라이버가 다운이 안 될까... 결국 수동으로 다운 받고 직접 파일 경로를 지정해줬다.
# service = Service("C:/Users/HOME/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# #service = Service(ChromeDriverManager(version="114.0.5735.90").install())
# driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()

# driver.get("https://google.com")
# print(driver.title)
# print(driver.current_url)

# #무한 스크롤페이지 스크롤 내리기
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #자바 스크립트 페이지 스크롤 처음부터 페이지 끝까지 내리기
# driver.implicitly_wait(5)

# #검색창
# search_input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]') 
# print(search_input)


# #검색어
# search_input.send_keys("파이썬 코딩연습")
# search_input.send_keys(Keys.ENTER)

# #검색어 삭제
# time.sleep(2)
# # time.sleep(2)
# # search_input.clear()

# # email_text  =driver.find_element(By.XPATH, '//*[@id="gb"]/div[2]/div[3]/div[1]/div/div[1]/a')
# # href = email_text.get_attribute("href")
# # print(href)

# #폴더 경로 지정해서 스샷 저장하기
# driver.save_screenshot("./1204/save.png") 


# input("대기")

#실습1. github 크롤링

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import time

# #옵션 객체
# options = Options()


# options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe" 
# #왜 나는 자동으로 크롬 드라이버가 다운이 안 될까... 결국 수동으로 다운 받고 직접 파일 경로를 지정해줬다.
# service = Service("C:/Users/HOME/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()

# #옵션 추가
# options.add_argument("--start-maximized")
# #options.add_argument("--headless")
# options.add_argument("--incognito") #로그인하기 위해 시크릿 모드 옵션 켜기

# #웹사이트 지정 -나는 클릭이 안 먹혀서 로그인 페이지부터...
# driver.get("https://github.com/login")
# print(driver.title)
# print(driver.current_url)


# #로그인 버튼
# #signin_click = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/header/div/div[1]/div[2]/a')
# #print(signin_click)
# #time.sleep(7)

# #signin_click.click()

# #이메일
# emailadd = driver.find_element(By.XPATH, '//*[@id="login_field"]')
# emailadd.send_keys("Sojung-Oh")

# #password

# passwd = driver.find_element(By.XPATH, '//*[@id="password"]')
# passwd.send_keys("dhthfl545400")

# button = driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
# button.click()

# #finding profile

# proftab1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div[3]/deferred-side-panel/include-fragment/react-partial-anchor/button/span/span/img')
# proftab1.click()

# time.sleep(5) #로딩이 느려 element가 활성화 안 된 경우도 있어 추가함

# proftab2 = driver.find_element(By.XPATH, '//*[@id=":rf:--label"]')
# proftab2.click()

# #printing user profile info
# time.sleep(5) #로딩이 느려 element가 활성화 안 된 경우도 있어 추가함
# username = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/div/div/div[1]/div/div/div[1]/div[2]/h1/span[2]')
# print("사용자명: ", username.text)

# usermail = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/main/div/div/div[1]/div/div/div[3]/div[2]/ul/li/a')
# print("사용자 이메일: ", usermail.text)

# time.sleep(3)
# #input("대기")

# driver.quit()

#실습2. 쇼핑몰 크롤링하기


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import time

# #옵션 객체
# options = Options()

# options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe" 
# #왜 나는 자동으로 크롬 드라이버가 다운이 안 될까... 결국 수동으로 다운 받고 직접 파일 경로를 지정해줬다.
# service = Service("C:/Users/HOME/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()

# #옵션 추가
# options.add_argument("--start-maximized")

# #웹사이트 지정 -온라인 쇼핑몰
# driver.get("https://www.lge.co.kr/")
# print(driver.title)
# print(driver.current_url)

# #검색창에 노트북 입력
# button1 = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[5]/div[1]/div[2]/ul/li[1]/a')
# button1.click()
# time.sleep(1)

# searchtab = driver.find_element(By.XPATH, '//*[@id="layerSearch"]/div/div/div[1]/div/div/form/input')
# searchtab.send_keys("노트북")
# searchtab.send_keys(Keys.ENTER)

# time.sleep(4)
# #상품 정렬 순서 가격순으로 바꾸기

# ordertab = driver.find_element(By.XPATH, '//*[@id="cusomtSelectbox_57_button"]/a/span[1]')
# ordertab.click()
# time.sleep(1)
# #가격 높은 순서대로 정렬
# price_order = driver.find_element(By.XPATH, '//*[@id="cusomtSelectbox_57_menu"]/div[1]/ul/li[3]/a')
# price_order.click()

# time.sleep(5)

# #가격 높은 순에서 첫번째 상품 선택
# highest = driver.find_element(By.CLASS_NAME, 'result-list.item-card-wrap.more')
# highest.click()

# time.sleep(3)

# #선택된 상품 페이지에서 상품 이름과 가격 추출하기

# prod_name = driver.find_element(By.XPATH, '//*[@id="typeOrder"]/div[2]/div[2]/div[1]/div[1]/div[2]/h1')
# print("상품명: ", prod_name.text)

# original_price = driver.find_element(By.XPATH, '//*[@id="b2cPriceArea"]/ul/li[1]/dl/dd/div/small')
# print("원가: ", original_price.text)

# dis_price = driver.find_element(By.XPATH,'//*[@id="maxBenefitPopupSelector"]/span')
# print("할인가: ", dis_price.text)

# driver.quit()

#실습3. 여행사이트 크롤링하기 (부킹 닷컴)

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
options.add_argument("--disable-notifications")
options.add_argument("--incognito")

options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe" 
#왜 나는 자동으로 크롬 드라이버가 다운이 안 될까... 결국 수동으로 다운 받고 직접 파일 경로를 지정해줬다.
service = Service("C:/Users/HOME/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

#웹사이트 지정 -부킹 닷컴
driver.get("https://www.booking.com/")
print(driver.title)
print(driver.current_url)

time.sleep(2)
# driver.refresh()

#로그인 팝업창 닫기

#driver.find_element(By.XPATH, '//*[@id="b2indexPage"]/div[44]/div/div/div/div[1]/div[1]/div/button').click()

city = driver.find_element(By.XPATH, '//*[@id=":rh:"]')
city.send_keys("후쿠오카 공항")

time.sleep(2) 
#계속 서울로 검색되던 원인...미처 후쿠오카 공항을 사이트에 검색하기 전에 엔터가 입력되어서 그런듯
#시간 텀을 주니까 해결되었다.
city.send_keys(Keys.ENTER)

time.sleep(2)

next_page = driver.find_element(By.XPATH, '//*[@id="calendar-searchboxdatepicker"]/div/div[1]/button')
next_page.click()

start_date = driver.find_element(By.XPATH, '//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[2]/table/tbody/tr[2]/td[4]')
start_date.click()

end_date = driver.find_element(By.XPATH, '//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[2]/table/tbody/tr[3]/td[2]/span')
end_date.click()

driver.find_element(By.XPATH, '//*[@id="bodyconstraint-inner"]/div[2]/div/div[1]/div/form/div/div[4]/button').click()

time.sleep(3)

#hotels = driver.find_elements(By.CSS_SELECTOR, "div .d4924c9e74")
 
#name = driver.find_element(By.CSS_SELECTOR, 'div .d4924c9e74 > div > div > div > div > div > div > div > div > h3 > a > div')
#print(name.text)



input("대기")

