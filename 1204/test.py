from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Chrome 옵션 설정
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--incognito")

# 특정 ChromeDriver 버전을 설치
chrome_driver_path = ChromeDriverManager().install()

# WebDriver 설정
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# 테스트 실행
driver.get("https://google.com")
print(driver.title)
driver.quit()
