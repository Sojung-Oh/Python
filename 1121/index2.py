#리스트 기초

# number = [1, 2, 3, "Hello", "Python"]
# print(number[3])

#리스트 슬라이싱
# shop = ["반팔", "청바지", "이어폰", ["무선키보드", "기계식키보드"]]
# print(shop[:2]) # 0 <= shop < 2
# print(shop[3])
# print(shop[-2])

# shop[0] = "긴팔"
# print(shop) 
# # shop[100] = "신발" #없는 인덱스에 접근하려고 하면 오류 발생!
# # print(shop)
# del shop[1]
# print(shop)
# del shop[2:]
# print(shop)

"""
a = [1, 2, 3]
b = ["안녕하세요", "반갑습니다"]
print(a + b)
print(b * 3)"""

#정렬함수

# num = [3, 1, 5, 2]
# num_asc = sorted(num)
# print(num_asc)

# num_dsc = sorted(num, reverse = True)
# print(num_dsc)
# print(num) # 원본은 변경되지 않았다.


# num.sort() # 메서드

# print(num)

# korean = ["강", "이", "박", "최", "강"]
# korean.sort(reverse)


# alphabet = 'b', 'b'

# a = ["a", "b", "c", "안녕", "Hi"]
# a.append("Good")
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)
# a.remove("안녕")
# print(a)
# a.insert(2, "잘가")
# print(a)
# a.clear()
# print(a)

# x = ['q', 'w', 'e', 'r', 'w']
# print(x.count('w'))

# 실습. 리스트 연습문제

# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# print("#1. 2번 인덱스 값 출력: ", rainbow[2])
# print("#2. 알파벳 순서로 정렬한 값 출력: ", sorted(rainbow))
# rainbow.append('pink')
# print("#3. 좋아하는 색 맨 마지막에 추가하기: ",rainbow) 

##print("#3. 좋아하는 색 맨 마지막에 추가하기: ",rainbow.append('pink')) 
#이거는 에러남!! 신기하네.... 메서드는 프린트문 안에 넣지 않기! 오류 나니까!

# #모범 예시 del rainbow[3:7]

# rainbow.pop(2)
# rainbow.pop(2)
# rainbow.pop(2)
# rainbow.pop(2)
# #print(rainbow)
# # r = r.pop(2)
# # r = r.pop(2)
# # r = r.pop(2)

# print("#4. 3~6번째 값 삭제하기: ", rainbow)

# 이차원 리스트

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9] 
# ]

# print(matrix[2][0])

# # 요소 추가
# matrix[1] = matrix[1] + [99]

# #print(matrix)

# #행 추가
# matrix = matrix + [[10, 11, 12]]
# print(matrix)

# #요소 수정
# matrix[0][0] = 100
# matrix[1][1] = 5000
# print(matrix)

# # 행 삭제

# del matrix[2]
# print(matrix)

# #행 개수
# rows = len(matrix)
# print(rows)
# #열 개수
# cols = len(matrix[0])
# print(cols)

# 이차원 메서드

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9] 
# ]

# # 요소 추가
# matrix[0].append(10)
# print(matrix)
# #행 추가
# matrix.append([10,11,12])
# print(matrix)
# matrix[1].insert(1,100)
# print(matrix)
# matrix.insert(2,["안녕하세요", "반갑습니다", "어서오세요"])
# print(matrix)

# #확장 extend
# matrix[0].extend([11, 12])
# print(matrix)

# 튜플 실습
# t1 = (1, )
# print(t1[0])
# t2 = (1, 2, 3, 4, 5, 3, 3, 3, 3)
# t3 = 1, 2, 3 #이것도 튜플!
# t4 = ('a', 'b', 'c', ("안녕", "감사"))
# print(t2.count(3))
# print(t3.index(2))
# print(t4[3],[0])
# print(len(t4))
# print('c' in t4) #튜플은 추가 수정 삭제 기능만 아니면 다 된다!

# Set 실습
# s1 = {1,1,1,1,1,1,2}
# print(s1) #{1, 2}
# s2 = ["안녕", "잘가", "hi", "안녕"]
# print(set(s2))


# s1 = {1, 2, 3, 3, 4}
# print(s1)
# s1.add(5)
# print(s1)
# s1.update([6, 7, 8, 9, 10])
# print(s1)
# s1.remove(3)
# print(s1)
# s1.discard(9)
# print(s1)
# # s1.remove(11)
# # print(s1) #error
# s1.discard(11)
# print(s1)
# s1.clear()
# print(s1)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
# s3 = s1 | s2 #합집합
s3 = s1.union(s2)
print(s3)

#교집합
#s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)

#차집합
s3 = s1 - s2
print(s3)