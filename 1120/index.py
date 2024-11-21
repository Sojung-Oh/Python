"""

print("안녕하세요")
print("hello", "python")
print("hello", "python", sep="|")
print("안녕하세요", end = "")
print("저는 오소정입니다")
print(1111111)

singer = input("좋아하는 가수는? ")
print("좋아하는 가수는 ", singer, "입니다")

#한 줄 주석에 사용
"""

"""
x = 10
print("before x:", x, id(x))
y, z = 3.14, "안녕하세요"
print("y: ", y)
print("z: ", z)
x = "hello"
print("after x:", x, id(x))

x = 10
print("after x:", x, id(x))

a = [1, 2, 3]
print("before a", a, id(a))
a.append(4)
print("after a", a, id(a))"""


# x = 48/2*(9+3)
# print(x)

# num = 5
# # += 5 ===> num = num +5
# num += 5
# print("+=", num)

# num -= 2 # num = num - 2
# print("-=", num)

# num *= 6 # num = num * 6
# print ("*=", num)
# num /= 2 # num = num/2
# print("/=", num)
# num //= 5 # num = num // 5
# print("//=", num)
# num %= 3 # num = num % 3
# print ("%=", num)

# a = 2 > 1 # True
# b = 3 < 2 # False
# c = 1 == 1 #True
# d = 3 >= 4 #False

# print( a and c) # True
# print(a and d) # False

# print (b or c) # True
# print(b or d) #False

# print(not a) #False
# print(not d) #True

# a = "hello world"
# print("H" in a) # False
# print("h" in a) #True
# print("a" not in a) #True
# print("w" not in a) #False

a = input("입력할 숫자는? : ")
a = int(a)

r = a % 2
b = r == 0
print("True면 짝수, False면 홀수: ", b)