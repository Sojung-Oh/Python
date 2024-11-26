# 함수

# def say_hello(born, name):
#     age = 2024 - born
#     print(f"{name}님의 나이는 {age}입니다.")

# say_hello(2000, "민지")

# #곱셈 함수
# def gugudan(dan, end):
#     print(f"{dan}단")
#     for i in range(1, end + 1):
#         print(f"{dan} X {i} = {dan * i}")

# gugudan(4, 20)

#결과 값이 있는 함수 (매개 변수의 유무 상관 없음)
# def calc_sum(num1, num2):
#     total = 0
#     for i in range(num1, num2 + 1):
#         total += i
#     return total

# result = calc_sum(10, 20)
# print(result)

# def fruits():
#     return ["사과", "바나나", "복숭아"]

# print(fruits())

# def students():
#     return {
#         "name": "홍길동",
#         "age": 20,
#         "major": "컴퓨터 공학"
#     }

# print(students())

#실습1

# def power_add(num1, num2):
#     if num1 == num2:
#         print("결과(곱): ", num1 * num2)
#     else:
#         print("결과(합): ", num1 + num2)

# power_add(2, 2)
# power_add(2, 3)

# 실습2.

# def d_price(price):
#     if price < 20000:

#         return price +2500
#     else:
#         return price
    
# print("상품 1 가격: 30000원 \n상품 1 가격 + 배송비", d_price(30000))
# print("상품 2 가격: 17500원 \n상품 2 가격 + 배송비", d_price(17500))

# 함수 매개변수로 리스트 전달
# def times(nums):
#     return [ i** 2 for i in nums]

# number = [2, 3, 6, 9]

# print(times(number))  #새로운 리스트가 전달된다.

#실습3. 자판기 프로그램 함수화

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비','생수', '생수', '생수', '이프로']

def check_machine():
     print("남은 음료수: ", vending_machine)

def is_drink(drink):
    return drink in vending_machine

def add_drink(drink):
    vending_machine.append(drink)
    vending_machine.sort()
    return vending_machine

def remove_drink(drink):
     vending_machine.remove(minus)
     return vending_machine
      


while True:     
    check_machine()
    #print("사용자 종류를 입력하세요(소비자일 경우 \'소비자\', 또는 숫자 1을, 주인일 경우 \'주인\' 또는 숫자 2를 입력해주세요): \n 1. 소비자 \n 2.주인 \n ")

    inning = input("\n사용자 종류를 입력하세요(소비자일 경우 \'소비자\', 또는 숫자 1을, 주인일 경우 \'주인\' 또는 숫자 2를 입력해주세요): \n 1. 소비자 \n 2.주인 \n 3. 종료 \n ")

    if inning == "1" or inning == "소비자":
        pur = input("마시고 싶은 음료수를 입력하세요: ")
        if is_drink(pur):
             print(f"{pur} 드릴게요.")
             vending_machine.remove(pur)
        else:
             print(f"{pur}은 지금 없네요.")
    elif inning == "2" or inning == "주인":
        inning2 = input("원하시는 기능을 선택해주세요. (추가를 원하실 경우 \'추가\' 또는 숫자 0을, 삭제를 원하실 경우 \'삭제\' 또는 숫자 1을 입력해주세요): \n 1. 추가 \n 2. 삭제 \n")
        if inning2 == "1" or inning2 == "추가":
            check_machine()
            plus = input("추가할 음료수를 입력해주세요.: ")
            add_drink(plus)
            check_machine()
        elif inning2 == "2" or inning2 == "삭제":
            check_machine()
            minus = input("삭제할 음료수를 입력해주세요: ")
            if is_drink(minus):
                print("삭제 완료")
                remove_drink(minus)
                check_machine()
            else:
                    print(f"자판기 안에 {minus}가(이) 없습니다. \n")
                    check_machine()
        else:
                print("잘못된 입력입니다. (추가를 원하실 경우 \'추가\' 또는 숫자 1을, 삭제를 원하실 경우 \'삭제\' 또는 숫자 2를 입력해주세요): ") 
    elif inning == '3' or inning == '종료':
         print("자판기 프로그램을 종료합니다.")
         break 
    else:
        print("잘못된 입력입니다. 소비자일 경우 '소비자', 또는 숫자 1을, 주인일 경우 '주인' 또는 숫자 2를 입력해주세요): ")