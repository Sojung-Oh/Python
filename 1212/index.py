import cv2

# # image = cv2.imread('./1212/images.png')
# image = cv2.imread('./1212/images.png',cv2.IMREAD_GRAYSCALE) #흑백으로 이미지 창 열림
# image_color = cv2.imread('./1212/images.png')

# print(image.shape)
# print(image_color.shape)

# cv2.imshow('Grey image', image)
# cv2.imshow('Color image', image_color)


# # key = cv2.waitKey(0) #무한 대기

# # if key == ord('q'): #q를 입력 받았을 때만 처리한다
# #     print(chr(key))
# # #eprint(key)


# cv2.waitKey(0)

# cv2.imwrite('./1212/output-image.jpg', image)

#cv2.destroyAllWindows()


#--------------------------------------------------------------
#image_color = cv2.imread('./1212/images.png')

# gray = cv2.cvtColor(image_color, cv2.COLOR_RGB2GRAY)
# hsv = cv2.cvtColor(image_color, cv2.COLOR_BGR2HSV)

#resized = cv2.resize(image_color, (400, 300)) #가로 세로 길이 지정
#scale = 0.5
#resized = cv2.resize(image_color, None, fx = scale, fy = scale) #0.5의 비율로 가로 세로 줄이기, 길이는 None 으로 지정 없음

# roi = image_color[50:300, 100:300].copy #이미지 배열, 아예 원본 이미지를 바꿔버린다, copy를 붙여야 복사본으로 작업!, 이거는 xy가 아니라 yx 순서!

# cv2.imshow('Color Image', roi) #range of interest, 관심 영역 -> 이미지 값을 잘 알아둬야!

#--------------------------------------------------------------
# x값, y값 찾기
# def mouse_click(e, x, y, flag, param):
#     if e == cv2.EVENT_LBUTTONDOWN:
#         print(f"마우스 위치 : x = {x}, y = {y}")


# image_color = cv2.imread('./1212/images.png')

# cv2.imshow('image', image_color)

# #마우스 콜백 함수
# cv2.setMouseCallback('image', mouse_click) #윈도우 이름, 마우스 콜백 함수 우리가 정의한 거(argument 5개여야)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#------------------------------------------------------------------------------
#roi만 표시

#글로벌 변수
# start = None
# end = None

# def mouse_select(e, x, y, flag, param): #뒤에 2개 안 쓰지만 형식상 필요!
#     global start, end
#     if e == cv2.EVENT_LBUTTONDOWN: #클릭을 누르는 상태
#         start = (x, y)
#     elif e == cv2.EVENT_LBUTTONUP: #클릭을 뗀 상태
#         end = (x, y)
#         #영역 표시
#         roi = image_color[start[1]:end[1], start[0]: end[0]] #x, y축 순서 바꼈으니까! 0, 1 이 아니라 1, 0
#         cv2.imshow('select', roi)



# image_color = cv2.imread('./1212/images.png')

# cv2.imshow('image', image_color)

# #마우스 콜백 함수
# cv2.setMouseCallback('image', mouse_select)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#-------------------------------------------------------------------------------------------------

# #
import numpy as np #이동을 위해서 필요
# image_color = cv2.imread('./1212/images.png')

# #중심 좌표
# (h,w) = image_color.shape[:2] #슬라이싱
# center = (w // 2, h // 2) #몫


# #회전
# # matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
# # rotated = cv2.warpAffine(image_color, matrix, (w, h)) #원본, 변환 행렬


# #이동
# matrix = np.float32([[1, 0, 100], [0, 1, 50]]) #앞에 x 축 100, 뒤에 y축 50
# move = cv2.warpAffine(image_color, matrix, (w,h))

# cv2.imshow('image', move)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#----------------------------------------------------------------------------------
#실습1 . 이미지 처리

image_color = cv2.imread('./1212/images.png')

#1. 이미지를 읽어서 크기를 출력
print(f'이미지 크기: {image_color.shape}')

#2. 이미지를 흑백으로 변환하고 화면에 표시
image_gray = cv2.imread('./1212/images.png',cv2.IMREAD_GRAYSCALE) #흑백으로 이미지 창 열림
cv2.imshow('image_gray', image_gray)

#3. 이미지를 50% 크기로 축소 후 새로운 창에 표시

scale = 0.5
resized = cv2.resize(image_color, None, fx = scale, fy = scale) #0.5의 비율로 가로 세로 줄이기, 길이는 None 으로 지정 없음
cv2.imshow('image_0.5', resized)

#이미지를 90도로 회전 후 저장

#중심 좌표
(h,w) = image_color.shape[:2] #슬라이싱
center = (w // 2, h // 2) #몫
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image_color, matrix, (w, h)) #원본, 변환 행렬



cv2.waitKey(0)
cv2.imwrite('./1212/90rotation_image.jpg', rotated)

cv2.destroyAllWindows()

