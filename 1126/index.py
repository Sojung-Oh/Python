# 전역 변수

# quantity = 10

# def get_price(price):
#     price = price * quantity
#     return price

# print(f"{quantity}개의 가격은 {get_price(5000)}입니다")

# #지역 변수

# def oneUp():
#     x = 0
#     x += 1
#     return x

# print(oneUp())

#유효범위
# quantity = 10

# def price_sum(price):
#     quantity = 7
#     return price * quantity

# print(price_sum(2000))

# x = 0
# def oneUp():
#     global x
#     x += 1
#     return x

# print(oneUp())
# print(oneUp())
# print(oneUp()) #전역변수를 바꾸려고 시도
# print(x)

#기본 매개변수

# def pr_str(txt = "안녕하세요", count = 1):
#     for _ in range(count):
#         print(txt) #i 를 형식상으로만 넣어줬을 때는 _로 대체하기도

# pr_str()
# pr_str("hello", 5)
# pr_str()

# 함수 호출 키워드
def intro(name, age, city):
    print(f"이름은 {name}이고 나이는 {age}이고 사는 곳은 {city}입니다.")

# intro("홍길동", 23, "서울")
# intro(city = "서울", name = "임꺽정", age = 23)
# intro("홍길동", city = "부산", age = 25) #키워드 지정이 없는 애를 먼저 입력할 것! 순서에 맞게 써야 한다.
# intro(city = "부산", 25, name = "홍길동")
#intro( city = "부산", age = 25, "홍길동") #잘못 쓴 예시

# 가변 매개변수

# def calc_avg(*args): # *은 가변임을 표시, 함수 안에서는 쓸 필요 없음, 변수 들어가는 순간 튜플 형태로 묶임
#     print(args)
#     total = 0
#     for i in args:
#         total += i
#     avg = total / len(args)
#     return avg

# print(calc_avg(1, 2, 3, 4, 5, 6, 7, 8))

# def text_def(a, b, *args): #무조건 고정, 1:1 대응인 애들이 앞으로 가고 가변인 애들을 뒤로 빼줘야 한다!
#     print("test :", a)
#     print("test :", b)
#     print("args :", args)

# text_def("hi", 1,2,3,4,5) #튜플형태로 나온다

# def intro(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# intro(name = "홍길동", age = 20, city = "Seoul", gender = "female" )


#내장함수

#abs(정수) - 절댓값을 구하는 내장함수
# def my_abs(x):
#     if x < 0:
#         return -x
#     else:
#         return x
    
# print(my_abs(-10))
# print(my_abs(5))

#print(abs(-10.4))

#거듭제곱
# print(pow(2, 4))

# def my_pow(x, y):
#     num = 1
#     for i in range(y): #for _ in range(y) 도 가능
#         print(f"i = {i}, {num*x} = {num} X {x}")
#         num *= x
#     return num

# print(my_pow(3, 4))

# map()

# def square(x):
#     return x ** 3

# numbers = [2, 4, 6, 8]

# squared = list(map(square, numbers)) #list() 안 써주면 오류!

# #filter()
# def even_number(x):
#     return x % 2 == 0 # x % 2 == 0 을  True / False 개념으로 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(filter(even_number, numbers)))

#함수의 리턴 값 반환은 여러 개 반환 가능

# def get_return():
#     arr = ["사과", "바나나"]
#     dic = {
#         "name":  "홍길동",
#         "age": 20
#     }
#     num = 30
#     return arr, dic, num

# arrs, dics, nums = get_return() # 3개의 리턴값을 넘겨 받았으니 3개에 맞춰서 대입! 순서대로 써주기!
# print(arrs) 
# print(dics) 
# print(nums) 

#실습 4. 함수 만들기

# while True:
#     num = input("1 ~ 30까지의 자연수를 입력해주세요(종료를 원할 시 '종료'를 입력해주세요): ")
#     if int(num)>=1 and int(num)<=30:
#         i = 1
#         list = []
#         result = 1
#         while result <= 30:
#             result = i*int(num)
#             print(result, end = " ")
#             list.append(result)
#             i += 1
#             result = i*int(num)
        
#         print(f"\n{num}의 배수의 개수: ", len(list))


#     elif num == "종료":
#         break
#     else:
#         print("잘못된 입력입니다. \n")  ## 헉 나 필터 \도 안 쓰고 함수도 정의 안 했나!! 

# #실습 4.  함수 만들기

# list1 = [i+1 for i in range(30)] #리스트 내포 사용
# #print(list1)

# def byby(elem):
#     return elem % int_num == 0


# while True:
#     num = input("\n1 ~ 30까지의 자연수를 입력하세요 (프로그램 종료를 원할 시 '종료'를 입력해주세요): ")
#     if num.isdigit():
#         if int(num) >= 1 and int(num) <= 30:
#             int_num = int(num)
            
#             result = filter(byby, list1)
#             final = list(result)
#             print(final)
#             print(f"{num}의 배수의 개수: {len(final)}")
#         else:
#             print("잘못된 입력입니다.")
#     else:
#         if num == "종료":
#             break
#         else:
#             print("잘못된 입력입니다.") 

#-----------------------리더님 예시--------------------------------------
# #방법1
# def count(num):
#     lists = [i for i in range(1, 31) if 1 % num == 0]
#     counts = len(lists)
#     return lists, counts


# num = 3
# lists, counts = count(num)
# print(f"{num}의 배수: {lists}")
# print(f"{num}의 배수의 개수: {counts}")

# #방법2

# def count(num):
#     #중첩 함수 - 이 함수 내에서만 사용이 가능
#     def check(x):
#         return x % num == 0

#     lists = list(filter(check, range(1, 31)))
#     return lists, len(lists)

# num = 3
# lists, counts = count(num)
# print(f"{num}의 배수: {lists}")
# print(f"{num}의 배수의 개수: {counts}")

# 재귀 함수

# def sos(i):
#     print("help me!", i)
#     if i == 1:
#         return ""
#     else:
#         return sos(i-1)
    
# sos(10)

# 팩토리얼

# def factorial(n):
#     print("n의 값:", n)
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(3))

# 실습 5. 피보나치 수열 만들기

# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)
    
# print(fibonacci(6))


#람다식
#일반함수

# def add(x, y):
#     return x + y

# print(add(3, 4))

# add = lambda x, y : x + y #add라는 변수에 함수 담겨 있음
# print(add(4, 5)) # 쓸 때는 함수 쓰듯이


# oneup = lambda x : x + 1
# print(oneup(1))
# print((lambda x : x + 1)(2))

# square = lambda x: x ** 2
# print(square(4))
# print((lambda x: x ** 2)(5))

# minus = lambda x, y: x - y
# print(minus(10, 2))
# print((lambda x, y: x - y)(7,4))


# def call(func):
#     for _ in range(10):
#         func()

# def hello():
#     print("안녕하세요")

# hello2 = lambda: print("반갑습니다.")

# #call(hello)
# call(hello2)

# numbers = [2, 4, 6, 8]
# squared = map(lambda x : x ** 3, numbers)
# print(list(squared))  #map()와 filter()의 예시와 비교

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(filter(lambda x: x % 2 ==0, numbers)))

# #실습4. 함수 만들기 -람다식
# def count(num):
#     lists = list(filter(lambda x: x % num == 0, range(1, 31)))
#     return lists, len(lists)

# num = 5


#실습 6 힘수 종합 프로그램

weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2023-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]



def avg_temp(inn):
    result = []
    def check(inn):
        for i in range(len(weather_data)):
            if weather_data[i][1] == inn:
                result.append(weather_data[i][2])
            else:
                continue
        return result
    
    
    li_result = check(inn)
    #print(li_result)
    #print(len(li_result))
    return sum(li_result) / len(li_result)

#print(avg_temp("서울"))

def min_temp(inn):
    result = []
    def check(inn):
        for i in range(len(weather_data)):
            if weather_data[i][1] == inn: #기온 거르기
                result.append(weather_data[i][2])
            else:
                continue
        return result #도시 이름 걸러내기
    
    
    li_result = check(inn)
    #print(li_result)
    #print(len(li_result))
    return min(li_result)

#print(min_temp("서울"))

def max_temp(inn):
    result = []
    def check(inn):
        for i in range(len(weather_data)):
            if weather_data[i][1] == inn: #기온 거르기
                result.append(weather_data[i][2])
            else:
                continue
        return result #도시 이름 걸러내기
    
    
    li_result = check(inn)
    #print(li_result)
    #print(len(li_result))
    return max(li_result)

# print(max_temp("서울"))

def precip(inn):
    result = []
    def check(inn):
        for i in range(len(weather_data)):
            if weather_data[i][1] == inn: #강수량 거르기
                result.append(weather_data[i][3])
            else:
                continue
        return result #도시 이름 걸러내기
    li_result = check(inn)

    total = sum(li_result)
    count = 0

    for i in range(len(li_result)):
        if li_result[i] != 0:
            count += 1
        else:
            continue

    return total, count

# total, count = precip("서울")
# print(f"총 {total} mm, 총 {count} 일")

def add_data(date, city, temp, prec):
    emp = [date, city, float(temp), float(prec)]
    weather_data.append(emp)


def data_show():
    print("현재 저장된 날씨 데이터: \n")
    for i in range(len(weather_data)):
        print(f"날짜: {weather_data[i][0]}, 도시: {weather_data[i][1]}, 평균 기온: {weather_data[i][2]} celsius, 강수량: {weather_data[i][3]}mm")   

#data_show()
while True:
    print("[날씨 데이터 분석 프로그램] \n1.평균 기온 계산\n2.최고/최저 기온 찾기\n3.강수량 분석\n4.날씨 데이터 추가\n5.전체 데이터 출력\n6.종료(오소정)\n")
    inn = input("원하는 기능의 번호를 입력하세요: ")
    if inn == "1":
        inn2 = input("도시의 이름을 선택하세요(서울 부산 중 택 1): ")
        if inn2 == "서울" or inn2 == "부산":
            print(f"{inn2}의 평균 기온: {avg_temp(inn2):.2f} celsius \n\n\n")
        
        else:
            print("잘못된 입력입니다.")
    elif inn == "2":
        inn2 = input("도시의 이름을 선택하세요(서울 부산 중 택 1): ")
        if inn2 == "서울" or inn2 == "부산":
            print(f"{inn2}의 최고 기온: {max_temp(inn2)} celsius, 최저 기온: {min_temp(inn2)} celsius\n\n\n")
        
        else:
            print("잘못된 입력입니다.")
    elif inn == "3":
        inn2 = input("도시의 이름을 선택하세요(서울 부산 중 택 1): ")
        if inn2 == "서울" or inn2 == "부산":
            total, count = precip(inn2)
            print(f"{inn2}의 총 강수량: {total} mm\n{inn2}에 강수량이 있었던 날: {count}일\n\n\n")
        else:
            print("잘못된 입력입니다.")       
    elif inn == "4":
        date = input("\n날짜를 입력하세요. (YYYY-MM-DD): ")
        city = input("\n도시를 입력하세요.: ")
        temp = input("\n평균 기온을 입력하세요. (celsius): ")
        prec = input("\n강수량을 입력하세요.(mm): ")
        add_data(date, city, temp, prec)
        print(f"{city}의 날씨 데이터가 추가되었습니다. \n\n\n")
    elif inn == "5":
        data_show()
    elif inn == "6":
        break
    else:
        print("잘못돤 입력입니다.\n")
