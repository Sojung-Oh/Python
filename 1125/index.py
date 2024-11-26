#for 문
# 리스트와 for 문

# fruits = ["사과", "포도", "바나나", "복숭아"]
# for fruit in fruits:
#     print("과일은:", fruit )


# #합계 구하기
# number = [10, 20, 30, 40, 50]
# total = 0
# for num in number:
#     total += num
# print(f"리스트 값의 합계는 {total}입니다")


# # 조건문 사용
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in number:
#     if num % 2 == 0:
#         print(num, end = " ")

# #리스트 내포
# squares = [ i ** 2 for i in range(1, 20) ]
# print(squares)

# #if문과 함께 사용
# even_squares = [   i ** 2 for i in range(1,10) if i % 2 == 0]
# print(even_squares)

#딕셔너리와 for문
# my_dic = {
#     "name": "홍길동",
#     "address": "서울시 은평구",
#     "gender": "남자",
#     "hobby": ["런닝", "헬스", "낚시"]
# }

# # 키값만 순회
# # for i in my_dic:
# #     print(i, end = " ")
# # print()

# # for i in my_dic.keys():
# #     print(i, end = " ")
# # print()

# # for i in my_dic.values():
# #     print(i, end = " , ")
# # print()
# for key, value in my_dic.items():
#     print(f"{key}: {value}")

# JSON = 딕셔너리

# 실습. 구구단 만들기

# num = input("몇단을 출력할까요?: ")
# if num.isdigit():
#     for i in range(1, 10):
#         print( num, 'x', i,  '=', int(num) * i)

# else:
#     print("숫자만 입력하세요.")

#실습. 정수합 계산

# num = input("어디까지 계산할까요?: ")
# if num.isdigit():
#     total = 0
#     for i in range(1, int(num)+1):
#         if int(i) % 2 != 0:
#             total += i
#     print(f"1부터 {num}까지의 홀수의 합: {total}")
    

# else:
#     print("숫자만 입력하세요.")

#실습. 평균값 구하기
# stu = {
#     "stu1": [83, 92, 88],
#     "stu2": [90, 79, 86],
#     "stu3": [88, 86, 94]
# }
# total = 0
# iter = 0
# num =0

# for i in stu.values():
#     total = sum(i)
#     iter = len(i)
#     num += 1
#     print(f"학생{num}의 국, 영, 수 점수의 평균값은 {total/iter}이다.")


# # 리더님 예시

# students = {
#     "학생1": {"국어": 83, "영어": 92, "수학": 88},
#     "학생2": {"국어": 90, "영어": 79, "수학": 86},
#     "학생3": {"국어": 88, "영어": 86, "수학": 94},
# }

# for student, score in students.items():
#     print(student, score)
#     total = sum(score.values()) #세 과목의 합계
#     avg = total/len(score)
#     print(avg)
#     print(f"{student}의 평균은 {avg:.2f}")


#이중 for문
# for i in range(5):
#     for j in range(3):
#         print(f"i: {i}, j: {j}")
#     print()

#이차원 리스트와 for문

# matrix = [
#     [3, 6, 9, 12],
#     [2, 4, 6, 8],
#     [10, 20, 30, 40],
#     [11, 12, 13, 14]
# ]

# for row in matrix:
#     for elem in row:
#         if 

#실습. 이중 for문 구구단
#i단
# for i in range(2, 10):
#     print(f"[{i}단]")
#     for j in range(1, 10):
#         print(f" {i} X {j} = {i * j}")
#     print()

#과제. 자판기 프로그램

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비','생수', '생수', '생수', '이프로']
while True:     
    print("남은 음료수: ", vending_machine)
    #print("사용자 종류를 입력하세요(소비자일 경우 \'소비자\', 또는 숫자 1을, 주인일 경우 \'주인\' 또는 숫자 2를 입력해주세요): \n 1. 소비자 \n 2.주인 \n ")

    inning = input("사용자 종류를 입력하세요(소비자일 경우 \'소비자\', 또는 숫자 1을, 주인일 경우 \'주인\' 또는 숫자 2를 입력해주세요): \n 1. 소비자 \n 2.주인 \n 3. 종료 ")

    if inning == "1" or inning == "소비자":
        pur = input("마시고 싶은 음료수를 입력하세요: ")
        if pur in vending_machine:
            print(f"{pur} 드릴게요.")
            vending_machine.remove(pur)
        else:
            print(f"{pur}은(는) 지금 없네요.")
    elif inning == "2" or inning == "주인":
        inning2 = input("원하시는 기능을 선택해주세요. (추가를 원하실 경우 \'추가\' 또는 숫자 0을, 삭제를 원하실 경우 \'삭제\' 또는 숫자 1을 입력해주세요): \n 1. 추가 \n 2. 삭제 \n")
        if inning2 == "1" or inning2 == "추가":
            print("자판기 안의 음료수는 다음과 같습니다.: ", vending_machine)
            plus = input("추가할 음료수를 입력해주세요.: ")
            vending_machine.append(plus)
            vending_machine.sort()
            print("자판기 안의 음료수는 다음과 같습니다.: ", vending_machine)
        elif inning2 == "2" or inning2 == "삭제":
            print("자판기 안의 음료수는 다음과 같습니다.: ", vending_machine)
            minus = input("삭제할 음료수를 입력해주세요: ")
            if minus in vending_machine:
                vending_machine.remove(minus)
                print("자판기 안의 음료수는 다음과 같습니다.: ", vending_machine)
            else:
                    print(f"자판기 안에 {minus}가(이) 없습니다. \n자판기 안의 음료수는 다음과 같습니다.: ", vending_machine)
        else:
                print("잘못된 입력입니다. (추가를 원하실 경우 \'추가\' 또는 숫자 1을, 삭제를 원하실 경우 \'삭제\' 또는 숫자 2를 입력해주세요): ") 
    elif inning == '3' or inning == '종료':
         print("자판기 프로그램을 종료합니다.")
         break 
    else:
        print("잘못된 입력입니다. 소비자일 경우 '소비자', 또는 숫자 1을, 주인일 경우 '주인' 또는 숫자 2를 입력해주세요): ")


            



