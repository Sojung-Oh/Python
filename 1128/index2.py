# #상속
# #부모 클래스가 생성자가 없을 때

# class Animal:
#     def speak(self):
#         print("동물이 소리를 냅니다.")

#     def move(self):
#         print("동물이 움직입니다.")

# #자식 클래스
# class Cat(Animal):
#     def meow(self):
#         print("야옹!")
    

# cat = Cat() #생성자가 없으므로 그냥 이렇게 생성 가능
# cat.speak()
# cat.move() #자식클래스 인스턴스가 부모 클래스의 메서드 사용 가능
# cat.meow()


#부모 클래스의 생성자가 존재할 때

# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name}가 소리를 냅니다.")
    
#     def move(self):
#         print(f"{self.name}가 움직입니다.")

# #자식 클래스
# class Cat(Animal):                #야옹 은 기본 값!
#     def __init__(self, a, sound = "야옹"): #부모 클래스와 같이 생성자에 대한 처리를 해주어야 한다! 변수 추가 가능하지만 부모 먼저 관례상 입력
#         super().__init__(a) #부모 클래스에 있는 name 생성자를 '호출'하는 것!
#         self.sound = sound

#     def meow(self):
#         print(f"{self.name}가 {self.sound} 짖습니다.")
#                  #여기는 self.a 하면 안 됨 부모 클래스에서 호출하는 거니까!
# cat = Cat("Lemon") #값이 안 올 때는 기본 값 사용!
# cat.speak()
# cat.move()
# cat.meow()

#다중 상속 

##정보 은닉은 꼭 안 써도 됨! 게터 세터도 써도 되고 안 써도 된다
# class Engine:
#     def __init__(self,horsepower):
#         self.horsepower = horsepower
#         self.count = 100

# class Wheels:
#     def __init__(self, count):
#         self.count = count

# class Car(Engine, Wheels):
#     def __init__(self, horsepower, count, wheel_count):
#         Engine.__init__(self, horsepower, count)
#         Wheels.__init__(self, wheel_count) #여기는 self까지 써줘야!

#     def info(self):
#         print(f"이 자동차는 {self.horsepower} 마력과 {self.count}개의 바퀴를 가지고 있다.")
    
#     def test(self):
#         print(f"어디? {self.count}")

# ######---------------------동일한 값이 들어갔을 때 오류가 나타나며 앞에 있는 엔진의 카운트가 들어가야 하는데 왜 오류가 안 날까?
# car = Car(100, 50, 4)
# #car.info()
# car.test()
# print(Car.mro()) 

#오버라이딩
# class Parent:
#     def greet(self):
#         print("안녕하세요. 부모 클래스")

# class Child(Parent):
#     def greet(self): #같은 이름, 같은 매개변수 개수
#         super().greet() #부모클래스에 있는 greet() 호출
#         print("안녕하세요. 자식 클래스")

# p = Parent()
# c = Child()
# p.greet()
# print()
# c.greet()

# 실습. 상속과 오버라이딩

#부모 클래스
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     # 재고 업데이트 메서드
#     def update_quantity(self, amount):
#         self.quantity += amount
#         print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")

#     # 상품 정보 출력 메서드
#     def display_info(self):
#         print(f"상품명: {self.name}")
#         print(f"가격: {self.price}원")
#         print(f"재고: {self.quantity}개")

# # 자식 클래스

# class Electronic(Product):
#     def __init__(self, name, price, quantity, warranty_period = 12):
#         super().__init__(name, price, quantity)
#         self.warranty_period = warranty_period
    
#     def display_info(self):
#         super().display_info()
#         print(f"보증 기간: {self.warranty_period}개월")        

#     def extend_warranty(self, months):
#         self.warranty_period += months
#         print(f"보증 기간이 {months}개월 연장되었습니다. 현재 보증 기간:  {self.warranty_period}개월")

# class Food(Product):
#     def __init__(self, name, price, quantity, expiration_date):
#         super().__init__(name, price, quantity)
#         self.expiration_date = expiration_date

    
    
#     def is_expired(self, current_date):
#         if self.expiration_date < current_date:
#             print(f"{self.name}는(은) 유통기한이 지났습니다.")
#         else:
#             print(f"{self.name}는(은) 유통기한이 지나지 않았습니다.")

#     def display_info(self):

#         super().display_info()
#         print(f"유통 기한: {self.expiration_date}") 

# apple = Food("apple", 12, 20, "2024-12-25")
# apple.is_expired("2025-01-02")
# apple.display_info()

#추상화
#추상 클래스
# from abc import ABC, abstractmethod

# class PaymentSystem(ABC): #ABC를 꼭 상속받아야 추상화 가능!
    
#     #추상 메서드
#     @abstractmethod
#     def authenticate(self):
#         pass #무조건 패스!!  클래스의 개념이 약해서 오류는 나지 않지만 문법상 안 쓰는 게 좋다

#     @abstractmethod
#     def process_payment(self, amount):
#         pass

#     def payment_info(self, amount):
#         print(f"{amount}원 결제가 완료되었습니다.")

# class KakaoPay(PaymentSystem):
#     def authenticate(self):
#         print("카카오페이 인증 완료 되었습니다.")
    
#     def process_payment(self, amount):
#         print(f"카카오페이로 {amount}원을 결제합니다.")

# pay = 50000
# kakao = KakaoPay()
# kakao.authenticate()
# kakao.process_payment(pay)
# kakao.payment_info(pay)

#클래스 메서드

# class Converter:
#     conversion_rate = 1.60934

#     @classmethod
#     def miles_to_kilometer(cls, mile):
#         return mile * cls.conversion_rate

# print(Converter.miles_to_kilometer(7)) #인스턴스 선언하면 클래스 메서드인지 구분 어려우므로 하지 x

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         age = 2024- birth_year
#         return name, age

# #생성자가 아닌 클래스 메서드를 통해서 객체 생성!
# p1 = Person.from_birth_year("홍길동", 1990)
# #print(p1) #튜플 형태로 출력
# print(p1.name, p1.age)


#----------------클래스 변수를 사용하는 법
# class Counter:
#     count = 0 #클래스 변수

#     @classmethod
#     def increment(cls):
#         cls.count += 1

#     @classmethod
#     def get_count(cls):
#         return cls.count

# Counter.increment()
# Counter.increment()
# Counter.increment()
# print(Counter.get_count())

#자식 클래스의 정보유지
# class Animal:
#     species = "동물"

#     @classmethod
#     def get_species(cls):
#         return cls.species

# class Dog(Animal):
#     species = "진돗개"

# print(Animal.get_species())
# print(Dog.get_species()) #서브 클래스에서 호출할 때 서브 클래스의 정보를 유지 시켜준다.

# # 정적 메서드
# class MathUtils:
#     @staticmethod
#     def add(a,b):
#         return a + b
    
#     @staticmethod
#     def minus(a,b):
#         return a - b

# #어떤 기능을 다 모아두거나 굳이 인스턴스를 선언할 필요가 없을 땨

# print(MathUtils.add(30, 40))
# print(MathUtils.minus(10, 20))

# 실습. 클래스 종합 프로그래밍

#날짜별 전력량
electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6},
]

#추상 클래스 생성 
from abc import ABC, abstractmethod

class ElectricityData(ABC):
    
    def __init__(self, usage_data, total_usage = 0):
        self._usage_data = usage_data
        self._total_usage = total_usage

    #Getter
    @property
    def usage_data(self):
        return self._usage_data
    
    #Setter
    @usage_data.setter
    def usage_data(self, value):
        self._usage_data = value

    #Getter
    @property
    def total_usage(self):
        return self._total_usage
    
    #Setter
    @total_usage.setter
    def total_usage(self, value):
        self._total_usage = value


    #추상 메서드
    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    #일반 메서드
    
    def add_usage(self, date, usage): #새로운 날짜의 전력 사용량을 추가
        new_data = {
            "date": date,
            "usage": usage
        }

        self._usage_data.append(new_data)

    def remove_usage(self, date):
        self._usage_data = filter(lambda x: x["date"] != date, self._usage_data) #날짜 일치하지 않는 딕셔너리만 걸러냄
    
# 자식 클래스

class HomeElectricityData(ElectricityData):
    def calculate_total_usage(self): #전력 사용량 데이터를 기반으로 총 사용량 계산
        usage_data = map(lambda x: x["usage"], self._usage_data)
        #print(list(usage_data)) #----------이부분을 넣으면 왜 오류날까....
        list_usage_data = list(usage_data)
        #print(list_usage_data)
        total_sum = sum(list_usage_data)
        print(f"총 전력 사용량: {total_sum}")
        
    
    def get_usage_on_date(self, date): #특정 날짜의 전력 사용량을 반환
        the_data = filter(lambda x: x["date"] == date, self._usage_data) #날짜 일치하는 딕셔너리 찾기
        thedata = list(the_data)
        #print(thedata[0]['usage'])
        dt_usage = thedata[0]['usage'] #filter() 의 결과값이 항상 리스트? list() 함수는 프린트 내부에 쓰면 오류 나는 건가?
        print(f"{date}의 사용량: {dt_usage}")
    
    #클래스 메서드
    @classmethod
    def date_filtering(cls, date1, date2): # 클래스 메서드를 사용하여 electricity_usage 리스트에서 특정 날짜 범위 내의 데이터 필터링하는 기능 
        filtered_usage_data = filter(lambda x: x["date"] >= date1 and x["date"] <= date2, electricity_usage)
        list_filtered_data = list(filtered_usage_data)
        print(f"특정 날짜 범위 내 사용량: {list_filtered_data}")
    
    # 정적 메서드 
    @staticmethod
    def max_usage_data(): #정적 메서드를 사용하여 전력사용량 데이터에서 가장 높은 사용량을 찾는 기능
        list_usage = list(map(lambda x: x["usage"], electricity_usage))
        #print(list_usage)
        max_usage_value = max(list_usage)
        #print(max_usage_value)
        max_usage = filter(lambda x: x["usage"] == max_usage_value, electricity_usage)
        list_max_usage = list(max_usage)
        print(f"가장 높은 전력 사용량: {list_max_usage[0]}")

data1 = HomeElectricityData(electricity_usage)
data1._usage_data = electricity_usage
data1._total_usage = 0

data1.calculate_total_usage()
data1.add_usage("2024-11-06", 16.4)
data1.get_usage_on_date("2024-11-03")
print("2024-11-06 데이터 추가 후", end = "")
data1.calculate_total_usage()
data1.date_filtering("2024-11-02", "2024-11-04")
data1.max_usage_data()