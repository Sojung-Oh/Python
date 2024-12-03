#예외 처리

# try:
#     x = int(input("숫자를 입력하세요"))
#     result = 10 / x
# except ZeroDivisionError as e: #e는 변수, 에러의 e
#     print("예외 메시지: ", e)
# except ValueError as e:
#     print("예외 메시지: ", e)
# else:
#     print(f"result: {result}")
# finally:
#     print("프로그램이 종료됩니다.")

# try:
#     x = int(input("숫자를 입력하세요"))
#     result = 10 / x
# except (ZeroDivisionError, ValueError) as e: #e는 변수, 에러의 e
#     print("예외 메시지: ", e)
# else:
#     print(f"result: {result}")
# finally:
#     print("프로그램이 종료됩니다.")


# raise Exception("예외처리") #강제 오류 발생시키기

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("예외발생 ", e)
else:
    with open("result.txt", "w", encoding = "utf-8") as file:
        file.write(f"결과: {result}")