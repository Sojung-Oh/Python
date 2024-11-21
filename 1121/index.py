#변수의 사이즈 알아보는 방법
# from sys import getsizeof

# print(getsizeof(1))
# print(getsizeof("1"))

#변수의 자료형을 알아보는 방법

# print(type(1111))
# print(type(333.333))
# print(type("hello"))
# print(type(True))
# print(type(None))

#형변환

# a = input("입력할 숫자는? : ")
# a = int(a)

# r = a % 2
# b = r == 0
# print("True면 짝수, False면 홀수: ", b)

# print(int(5.5))
# a = "10"
# print(type(int(a)))
# print(type(a))

# num = 10
# print(type(str(num)))

# 문자열을 연산하는 방법

# a = "파이썬"
# print("안녕하세요 " + a + " 반갑습니다")
# #print("오류" + 1234)

# print("hey!" * 10)

# print("데이터 확인", a)

# korea_song = """
# 동해물과 백두산이 마르고 닳도록
# 하느님이 보우하사 우리나라 만세
# 무궁화 삼천리 화려강산
# 대한사람 대한으로 길이 보전하세
# """

# print(korea_song)

#따옴표 출력

# print(' "오늘 저녁 뭐 먹지?"라고 생각하는 중이다') 
# print(" '오늘 저녁 뭐 먹지?'라고 생각하는 중이다")

#이스케이프
# print("Hello\nWorld")
# print("Hello\tWorld")
# print("hello\\world")
# print('\'hello\'')
# print(" \"hello\" ")

#문자열 포매팅
# year = "올해는 %d년 %s의 해이다" % (2024, "용띠")
# year = "올해는 %d년 %s의 해이다" % (2025, "말띠")
# print(year)

#포맷코드 활용

# number = "저는 올해 %d살입니다" % 20
# print(number)
# calc = "20 나누기 3은 %.2f" %6.66
# print(calc)
# text = "저는 %-10s에서 살고있습니다." % "포천"
# print(text)
# char = "이모티콘은 %c 이것으로 할게요" %"🎶"
# print(char)

#formatting
# country = "South Korea"
# city = "Pocheon"
# people = "Korean"
# text = "저는 올해 {0}살 입니다".format(20)
# print(text)
# text = "저는 {0} 사람이며 {1}에 살고있습니다".format(country, city)
# print(text)
# text = "저는 {1} 사람이며 {0}에 살고있습니다".format(country, city)
# print(text)
# text = "제가 사는 {0}은 {a}에 있습니다".format(city, a = "한국")
# print(text)
# text = "중괄호 출력하고 싶을 때 {{ 중괄호 }}".format()
# print(text)
# text = "{}, {}, {}, {}".format(80, 90, 100, 200)
# print(text)
# a = "[{0:&^10}]".format("hey")
# print(a)

#f 문자열 포매팅
# name = "오소정"
# age = 25
# print(f"내 이름은 {name}입니다. 나이는 {age +1}입니다.")
# print(f"내이름 [{name :@^20}]")

#이스케이프 실습

# a = """
# |\\_/|
# |q p|   /}
# ( 0 )\"\"\"\\
# |\"^\"`    |
# ||_/=\\\\__|
# """
# print("실습1\n",a)

# f문자열 포매팅 실습

# name = "오소정"
# print("1) " + f"[{name :=^20}]")
# print("2) 문자열 실습입니다." + f"{{ 중괄호 }}를 출력해보세요.")

# 퀴즈
# a = "Hello, Python"
# print(a[7] + a[8] + a[9] + a[10] + a[11] + a[12])
# print(a[7:])

#슬라이싱 퀴즈
# a = "20240930"
# print(a[:4]+"년 " + a[4:6] + "월 " + a[6:] + "일 ")
# a = "Hello, Python"
# print(len(a))
# print(a.count('l'))

# 위치 찾기
# a = "Hello, Python"
# print(a.find("P"))
# print(a.find("s"))
# print(a.find("o")) #다수일 경우 가장 앞선 문자 찾기

# #다수일 경우
# first_o = a.find('o')
# print(first_o)
# second_o = a.find('o', first_o + 1)
# print(second_o)

# print(a.index("P"))
# print(a.index("s")) #error

# 바꾸기, 나누기
# a = "Hello, Python"
# print(a.replace("Python", "파이썬"))
# print(a.split("l"))

# 대/소문자 바꾸기
# a = "Hello, World"
# print(a.upper())
# print(a.lower())

# a = "       Hello        "
# print(f"[{a.rstrip()}]")
# print(f"[{a.lstrip()}]")
# print(f"[{a.strip()}]") #보통 제일 많이 쓰는 거!


# print("1234".isdecimal())
# print("1234".isdigit()) #많이 쓰는 건 이거! 
# print("1234".isnumeric())

# print("Hello".islower())
# print("HELLO".isupper())

#종합실습

#1번

name = input("실습1번)\n이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
print(f"안녕하세요! {name}님  ({age}세)")

#2번
name = input("\n\n실습2번)\n이름을 입력하세요: ")
byear = input("태어난 년도를 입력하세요: ")
tyear = input("올해 년도를 입력하세요: ")
b = int(byear)
t = int(tyear)
print(f"올해는 {tyear}년, {name}님의 나이는 {t-b+1}세 입니다")
