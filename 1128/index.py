# #실습. 건강상태 클래스 만들기

# class Health:
#     def __init__(self, name):
#         self._hp = 100
#         self._name = name  # 언더바 하나: 보안 언더바 두개: 아예 외부에서 차단, 프라이빗 상태

#     def get_name(self):
#         return self._name
    
#     def set_name(self,value):
#         self._name = value

#     def set_hp(self, value):
#         self._hp = value

#     def get_hp(self):
#         return self._hp
    
#     def exercise(self, hour):
#         self.set_hp(self._hp + hour)
#         print(f"{hour} 시간 운동했다.")

#     def drink(self, cups):
#         self.set_hp(self._hp - cups)
#         print(f"술을 {cups}잔 마셨다.")

#     def info(self):
#         print(f"{self.get_name()} - hp: {self.get_hp()}")


# p1 = Health("나몸짱")
# p1.exercise(5)

# getter, setter 데코레이터

class Person: #정보 은닉하는 사람 클래스
    def __init__(self, name, age):
        self.__name = name
        self.__age = age 
    
    #getter
    @property #바로 위에 있어야 함. 한 줄이라도 밑에 띄워 두면 함수를 인식하지 못함!
    def name(self):
        return self.__name
    
    #setter
    @name.setter
    def name(self, value):
        self.__name = value
    
    #getter
    @property
    def age(self):
        return self.__age
    
    #setter
    @age.setter
    def age(self, value):
        self.__age = value


p1 = Person("홍길동", 28)
print(p1.name)
print(p1.age)

p1.name = "이몽룡"
p1.age = 25

print(p1.name)
print(p1.age)