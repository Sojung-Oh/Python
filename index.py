#딕셔너리
#생성
# dict1 = {}
# dict1 = dict()
# print(dict1)

# dict1 = {
#     "name": "홍길동",
#     "age": 20,
#     "city": "서울",
#     "hobby": ["런닝", "등산", "헬스"]
# }
# print(dict1)

# dict2 = dict(name = "홍길동", age = 20)
# print(dict2)
# print(dict1["name"])
# print(dict1["hobby"][2])

# #값 수정
# dict1["age"] = 21
# print(dict1)

# #값 추가
# dict1["birthday"] = 20001011
# print(dict1)
# dict1['hobby'] = ['런닝', '등산', '헬스', "캠핑"]
# print(dict1)
# del dict1["birthday"]
# print(dict1)

# #딕셔너리 메서드
# fruits = {
#     "apple": "사과",
#     "banana": "바나나",

# }
# print(fruits.get("apple"))
# print(fruits.get("peach")) #None
# print(fruits.get("peach", "복숭아")) # 복숭아

# #여러 요소 추가
# fruits.update({
#     "grapes": "포도",
#     "melon": "멜론"
# })
# print(fruits)
# print(fruits.keys())
# print(fruits.values())
# print(fruits.items())
# fruits.clear()
# print(fruits)

#실습_성적 관리

# student = {
#     "Alice" : 85,
#     "Bob" : 90,
#     "Charlie" : 95
# }
# print("2.", student)

# student["David"] = 80
# print("3.", student)
# student["Alice"] = 88
# print("4.", student)
# del student["Bob"]
# print("5.", student)

#내장함수
#sum()
# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))


# scores = {
#     "국어": 90,
#     "영어": 80,
#     "수학": 85
# }
# print(sum(scores.values()))

#zip()
names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 90, 88, 95]  # 두 개의 리스트

zipped = list(zip(names, scores)) # 리스트가 아닌 것 리스트로 표현, 
#안에 있는 것들은 튜플의 형태 왜냐하면 반환하는 것들은 변형하지 않고 사용하기 위해서!
print(zipped)