#클래스

#클래스 정의
# class Car: #대문자!
#     model = ""
#     cc = 0

#     #함수 추가
#     def info(self):
#         print(f"모델명 : {self.model}, 배기량: {self.cc}cc")

# # 사용

# car1 = Car() #인스턴스 생성
# car1.model = "싼타페"
# car1.cc = 2000

# # print(f"모델명: {car1.model}")
# # print(f"배기량: {car1.cc}cc")

# car1.info()

#생성자가 존재할 때

# class Car:

#     def __init__(self, model, cc):
#         self.model = model
#         self.cc = cc

#     #특수 메서드
#     def __str__(self):
#         return f"모델명: {self.model}, 배기량: {self.cc}cc"

#     def info(self):
#         print(f"모델명: {self.model}, 배기량: {self.cc}cc")


# car1 = Car("싼타페", 2000) #생성할 때 값을 넣어줌!
# car2 = Car("BMW", 2200)

# # car1.info() #출력 메서드
# # car2.info()
# print(car1)

# print("========== 승용차 리스트===========")
# cars = [
#     Car("소나타", 2000),
#     Car("쏘렌토", 3000),
#     Car("아반떼", 1600)
# ]

# for car in cars:
#     print(car)

# 실습1. 사칙연산 클래스 만들기

# class Four:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
    
#     def my_add(self):
#         return self.first + self.second
#     #def my_add(self,num):
#     #    return self.first + self.second+num
    
#     def my_sub(self):
#         return self.first - self.second
    
#     def my_mul(self):
#         return self.first * self.second
    
#     def my_div(self):
#         if self.second == 0:
#             return "분모가 0이 될 수 없습니다" #항상 오류 처리 조건은 위에 쓰기! 리턴은 여기서 함수를 끝낸다는 의미라 굳이 else를 안 써도 여기서 나감 
#         return self.first / self.second
    
    
# num1 = Four(20, 5)

# print(f" first num: {num1.first}, second num: {num1.second}")
# print(f"Addition: {num1.my_add()}")
# print(f"Subtraction: {num1.my_sub()}")
# print(f"Multiplication: {num1.my_mul()}")
# print(f"Division: {num1.my_div()}")


# 클래스 변수와 인스턴스 변수

# class Dog:
#     kind = "진돗개" #클래스 변수

#     def __init__(self, name):
#         self.name = name #인스턴스 변수


# dog1 = Dog("백구")
# dog2 = Dog("초코")
# print(dog1.name)
# print(dog2.name)

# # 클래스 변수 접근
# # print(dog1.kind)
# # print(dog2.kind) #이렇게는 잘 안 쓴다. 다른 사람이 봤을 때는 이게 클래스 변수인지 인스턴스 변수인지 알 수 없으니까

# print(Dog.kind) # 이런 식으로 클래스이름.클래스변수 

# class Example:
#     shared = "공유 변수" #클래스 변수

#     def __init__(self, name):
#         self.name = name #인스턴스 변수

# e1 = Example("A")
# e2 = Example("B")

# Example.shared = "변경된 공유 변수"

# print(e1.shared)
# print(e2.shared) 
# e1.name = "C"
# print(e1.name)
# print(e2.name) #인스턴스의 변경은 공유되지 않는다

# 사번 자동 발급
# class Employee:
#     serial_num = 1000 #클래스 변수

#     def __init__(self, name):
#         #클래스 변수 1씩 증가
#         Employee.serial_num += 1 #인스턴스 변수에만 셀프 쓰고 클래스 변수에는 셀프 쓸 필요 없음 
#         self.id = Employee.serial_num #사번
#         self.name = name
    
#     def __str__(self) -> str:
#         return f"사번 : {self.id}, 이름 : {self.name}"
    
# e1 = Employee("홍길동")
# print(e1)
# e2 = Employee("임꺽정")
# print(e2)

# employees = [Employee("이몽룡"), Employee("심청이"), Employee("변사또"), Employee("전우치")]

# for employee in employees:
#     print(employee)

# 실습2. Supermarket 클래스

# class Supermarket:
#     total_customer = 0
#     def __init__(self, location, name, product, customer):
#         self.location = location
#         self.name = name
#         self.product = product
#         self.customer = customer
#         Supermarket.total_customer += customer
    
#     def print_location(self):
#         print(f"위치 : {self.location}")
    
#     def change_category(self, product):
#         self.product = product
    
#     def show_list(self):
#         print(f"상품 : {self.product}")

#     def enter_customer(self):
#         #self.customer += 1
#         Supermarket.total_customer += 1
    
#     def show_info(self):
#         print(f"가게 이름: {self.name}")
#         print(f"위치: {self.location}")
#         print(f"상품: {self.product}")
#         print(f"손님 수: {Supermarket.total_customer}\n\n\n")

# sup1 = Supermarket("마포구 염리동", "마켓온", "음료", 12)
# sup2 = Supermarket("마포구 신설동", "마켓플리", "라면", 7)
# sup1.show_info()
# sup2.show_info()

# sup1.enter_customer()
# sup1.enter_customer()
# sup1.enter_customer()
# sup1.enter_customer()

# sup1.show_info()
# sup2.show_info()

# 정보 은닉

# class Person:
#     def __init__(self) -> None:
#         self._name = ""
#         self._age = 0  #외부에서 접근하지 않을 거라는 의미!

#     #이름을 설정
#     def setname(self, name):
#         self._name = name
    
#     #이름을 출력
#     def getname(self):
#         return self._name
    
#     #나이를 설정
#     def setage(self, age):
#         self._age = age
    
#     #나이를 출력
#     def getage(self):
#         return self._age

# p1 = Person()
# p1.setname("홍길동")
# print(p1.getname())

# p1.setage(20)
# print(p1.getage()) #정보 은닉을 위함

# 실습3. 건강 상태 클래스 만들기
class Health:

    def __init__(self) -> None:
        self._name = ""
        self._hp = 100
    
    def setname(self, name):
        self._name = name
    
    def getname(self):
        return self._name
    
    def sethp(self, hp):
        self._hp = hp
    
    def getage(self):
        return self._hp

    def workout(self, hour):
        self._hp += hour
        print(f"{hour} 시간 운동하다.")

        if self._hp > 100:
            return 100
        return self._hp


    def drink(self, cup):
        self._hp -= cup
        print(f"술을 {cup} 잔 마시다.")
        if self._hp < 0:
            return 0
        return self._hp
    
    def show_hp(self):
        print(f"{self._name}  -  hp: {self._hp}")

# p1 = Health()
# p1.setname("나몸짱")
# p1.sethp(98)
# p1.workout(5)
# p1.drink(12)
# p1.show_hp()

a = "[{0:,}]".format(12345678900)
print(a)


