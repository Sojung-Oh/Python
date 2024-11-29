#모듈

#import calc
#import calc as a #별칭 형태
#from calc import add, sub #add, sub 만 쓸 수 있는 상태
#from calc import add as a, sub as b
from calc import * #전부 다 가져오기

#모듈명. 함수명
print(add(10, 4))
print(sub(10, 4))
print(multiply(10, 4))
print(divide(10, 4))