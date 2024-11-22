# age = 21

# if age < 20:
#     print("미성년자입니다")

# print(f"나이는 {age}입니다")

#실습.if ~ else

# #1
# pw = input("비밀번호를 입력하세요: ")

# if pw == "abc123":
#     print("비밀번호가 맞습니다.")
# else:
#     print("비밀번호가 틀렸습니다.")

# #2
# num = input("숫자를 입력하세요: ")
# inum = int(num)
# if inum%2 == 0:
#     print("짝수입니다.")
# else: 
#     print("홀수입니다.")

#elif 문
# age = int(input("나이를 입력하세요: "))

# if age < 20:
#     print("10대입니다")
# elif age < 30:
#     print("20대입니다")
# elif age < 40:
#     print("30대입니다")
# elif age < 50:
#     print("40대입니다")
# else:
#     print("50대 이상입니다.")

#elif 실습

# score = int(input("점수를 입력하세요: "))

# if score >= 90:
#     print("학점: A")
# elif score >= 80:
#     print("학점: B")
# elif score >= 70:
#     print("학점: C")
# elif score >= 60:
#     print("학점: D")
# else:
#     print("학점: F")

#실습 중첩 조건문

# age = int(input("나이를 숫자로 입력해주세요: "))
# pur = input("결제 방법을 입력해주세요(현금 또는 카드): ")

# if age > 0:
#     if age < 8:
#         print(f"{age}세의 {pur} 요금은 무료입니다.")
#     if age < 14:
#         if pur == "카드":
#             print(f"{age}세의 {pur} 요금은 450원입니다.")
#         elif pur == "현금":
#             print(f"{age}세의 {pur} 요금은 450원입니다.")
#         else:
#             print("결제 방법을 카드와 현금 중 하나만 선택해 입력해주세요.")
#     elif age < 20:
#         if pur == "카드":
#             print(f"{age}세의 {pur} 요금은 720원입니다.")
#         elif pur == "현금":
#             print(f"{age}세의 {pur} 요금은 1000원입니다.")
#         else:
#             print("결제 방법을 카드와 현금 중 하나만 선택해 입력해주세요.")
#     elif age < 75:
#         if pur == "카드":
#             print(f"{age}세의 {pur} 요금은 1200원입니다.")
#         elif pur == "현금":
#             print(f"{age}세의 {pur} 요금은 1300원입니다.")
#         else:
#             print("결제 방법을 카드와 현금 중 하나만 선택해 입력해주세요.")
#     else:
#         print(f"{age}세의 {pur} 요금은 무료입니다.")
# else:
#     Print("나이는 양수로 입력해주세요.")

# 삼항 연산자

# age = int(input("나이를 입력하세요: "))
# #message = "20대입니다 " if age < 30 and age >= 20 else "20대가 아닙니다."
# message = "20대입니다 " if age < 30 and age >= 20 else "30대입니다." if age < 40 and age >= 30 else "20대도 30대도 아님니다."
# print(message)

#조건문에서 in 연산자
# fruit = input("과일을 한글로 입력하세요: ")

# if fruit in ["사과", "바나나", "복숭아"]:
#     print(f"{fruit}은(는) 과일에 포함되어 있습니다.")
# else:
#     print("존재하지 않는 과일입니다.")

# 실습. in 연산자 활용

# kcal = {
#     "apple" : 95,
#     "banana" : 105,
#     "cherry" : 50
# }

# name = input("과일을 영문으로 입력하세요: ")

# if name in kcal:
#     print(f"{name}의 칼로리는 {kcal[name]}kcal입니다.")
# else:
#     print(f"{name}은(는) 포함되지 않은 과일입니다.")

#합계 구하기

# num = 1
# total = 0
# while num <=10:
#     total += num  # total = total + num
#     num += 1 # 1부터 10까지의 합 구하기

# print(f"1부터 10까지의 합은 {total}입니다.")

#입력값 받기
# user_input = "" #빈 문자열 선언
# while user_input != "종료":
#     user_inut = input("원하는 값을 입력하세요. 종료하려면 '종료'를 입력하세요: ")
#     print(f"입력한 값: {user_input}")
# print("프로그램이 종료되었습니다.")  #게임 hp닳게 만들기 등에 활용 가능!

#break
# while True:
#     dinner = input("오늘 저녁 뭐먹지?: ")
#     if dinner == "제육":
#         break
#     print(f"오늘 저녁 메뉴는 {dinner}입니다.")
# print("저녁 메뉴 완료")

# count = 0

# while True:
#     print(count, end = " ")
#     count += 1
#     if count == 3:
#         break

# count = 0
# while count <10:
#     count += 1
#     if count % 2 == 0:
#         continue
#     print(count, end = " ")


# 실습 . while문 사용하기


# while True:

#     num = input("양수를 입력하세요('종료' 입력 시 프로그램 종료): ")

#     if num.isalpha():
#         if num == "종료":
#             print("프로그램을 종료합니다.")
#             break
#         else:
#             print("양수만 입력하세요.")
#     elif int(num) > 0:
#         i = 0
#         total = 0
#         while i <= int(num):
#             total += i
#             i += 1
        
#         print(f"1부터 n까지의 합은 {total}입니다.")

        
#     elif int(num) == 0:
#         continue
    
#     else:
#         print("양수만 입력하세요.")