#모듈

# #import calc
# #import calc as a #별칭 형태
# #from calc import add, sub #add, sub 만 쓸 수 있는 상태
# #from calc import add as a, sub as b
# from calc import * #전부 다 가져오기

# #모듈명. 함수명
# print(add(10, 4))
# print(sub(10, 4))
# print(multiply(10, 4))
# print(divide(10, 4))

from datetime import datetime, timedelta, timezone

# now = datetime.today()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# print(f"{now.year}년 {now.month}월 {now.day}일")

# now = datetime.now() #얘는 타임존 있음 UTC +9
# print(now) # 거의 똑같은 역할!

# #특정 날짜 계산
# next_week = now + timedelta(weeks = 1, hours = 1)
# print(next_week)

# 타임존 계산

# print(timezone.utc)
# print(datetime.now(timezone.utc))

# print(datetime.now(timezone(timedelta(hours = 9))))

# from datetime import date

# open_day = date(year = 2024, month= 11, day=18)
# print(date.today())
# print(date.today().weekday())
# week = ["월", "화", "수", "목", "금", "토", "일"]
# print(week[date.today().weekday()])

# pass_day = date.today() - open_day
# print(pass_day.days)

# import time

# print(time.time())
# print(time.localtime())
# print("2초 대기")
# time.sleep(2)
# print("대기 완료") #잠깐 멈추게 하기

# start = time.perf_counter() #시간 측정
# time.sleep(1)
# end = time.perf_counter()
# print(end - start)

# import math

# print(math.pi)
# print(math.sqrt(25))
# print(math.factorial(5))
# print(math.ceil(2.43)) #올림
# print(math.floor(4.88)) #버림
# print(round(2.5)) #반올림

# import random 
# import math

# print(random.randint(1000, 9999))
# print(random.uniform(1.1, 5.5))
# print(random.random())

# print(random.randrange(1000, 10000))
# choices = [1, 2, 3, 4, 5, 6, 7, 8]
# print(random.choice(choices))

# rand = 1000 + math.floor(random.random() * 9000) # 4자리의 난수 생성 (다른 언어에서 난수 생성 할 때 자주 사용하는 방식)
# print(rand)

#실습. 로또 번호 뽑기

# import random

# choices = list(range(1, 46))
# #print(choices)
# pick = []

# for i in range(6):
#     choice = random.choice(choices)
#     pick.append(choice)
#     choices.remove(choice)

# pick.sort()
# print(pick)

import sys

print(sys.argv) 
print(sys.argv[1:])

if "-h" in sys.argv or "--help" in sys.argv:
    print("사용법: python main.py [옵션]")
    print("-h, --help               도움말 표시")
    print("-v, --version            버전 정보 표시")
    sys.exit(0) # 프로그램 종료

if "-v" in sys.argv or "--version" in sys.argv:
    print("버전 : 1.0.0")
    sys.exit(0)


import os

# dir_current = os.getcwd() #현재 위치 나타내기
# print(dir_current)
# file_path = os.chdir(dir_current) #이 경로로 이동
# dir = os.popen('ls') #해당 폴더에 와서 ls로 조회
# print(dir.read()) #조회한 내용 읽어들이기

#os.mkdir("test") #test라는 폴더 생성하기
#os.rmdir("test")
#print(os.environ.get('PATH')) #환경 변수 출력

# import json

# data = {
#     "name": "홍길동",
#     "age": 20,
#     "city": "서울"
# }

# json_str = json.dumps(data)
# print(json_str)

# json_obj = json.loads(json_str) #파이썬 객체로 변환
# print(json_obj, json_obj["name"])

#실습 타자 연습 게임

#종료 조건 : 단어 3개 테스트

# import random, time
# words = ["mountain", "river", "forest", "ocean", "desert", "tree", "flower", "cloud", "rain", "sunlight"]
# num = 3 #입력해야할 단어 개수
# pick = random.sample(words, num)

# start = time.perf_counter() #시간 측정
# count = 0
# for i in range(num):
#     while True:
#         print(f"단어: {pick[i]}")
#         answer = input("입력: ")
#         count += 1
#         if pick[i] == answer:
#             print("통과!\n")
#             break
#         else:
#             print("오타! 다시 시도하세요.")


# end = time.perf_counter()
# print("\n게임 종료!")
# print(f"총 {num}개의 단어를 {count}회 입력하셨습니다.")
# print(f"총 걸린 시간: {end-start:.3f}")
# print(f"단어당 걸린 평균 시간: {(end-start)/num:.3f}")
# print(f"회 당 걸린 평균 시간: {(end-start)/count:.3f}")