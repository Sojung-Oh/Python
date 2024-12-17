"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("./1216/test_image.jpg")

# BGR -> HSV 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#색상 범위 설정 (빨강색)
lower = np.array([0, 120, 70]) #H, S, V 순서
upper = np.array([10, 255, 255])

#마스크 생성
mask = cv2.inRange(hsv_image, lower, upper)

#원본 이미지에 마스크 적용
result = cv2.bitwise_and(image, image, mask = mask) #원본 이미지, 채널 수가 같은 이미지 #두 이미지 간의 비트 연산

plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('mask')
plt.imshow(mask, cmap = 'gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('result')
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
"""

"""
#실시간 피부색 검출
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('웹캠을 열 수 없습니다')
    exit()

while True:
    ret, frame = cap.read()
    if not ret: # true false 값
        break

    #크기 변경
    frame = cv2.resize(frame, (640, 480))

    #HSV로 변경
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #피부색 범위(HSV)
    lower = np.array([0, 20, 70])
    upper = np.array([20, 255, 255])

    #마스크
    mask = cv2.inRange(hsv, lower, upper)

    #노이즈 제거(모폴로지 연산)
    mask = cv2.erode(mask, None, iterations=2) #입력 이미지, 채널 수 , 반복 횟수
    mask = cv2.dilate(mask, None, iterations=2)

    #컨투어 찾기
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #여기는 바꾸고 싶은 걸로 트리 말고 다른 걸로도 해보기

    #윤곽선 그리기
    for con in contours:
        area = cv2.contourArea(con)

        cv2.drawContours(frame, [con], -1, (0, 255, 0), 2) #초록색, 라인 두께 2

    cv2.imshow('skin', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

"""
"""
#----------------------------얼굴 인식
import cv2

#haar cascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('웹캠을 열 수 없습니다')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #얼굴 인식 알고리즘 위해서 먼저 그레이 스케일로 변환 필요!
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #얼굴 탐지
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)) #스케일 비율, 검출하는 사각형 수(높을 수록 정확), 사각형 크기

    #탐지된 얼굴에 사각형 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('face', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""
"""
#-------------얼굴, 눈 인식
import cv2

#얼굴
#haar cascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#눈
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('웹캠을 열 수 없습니다')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #얼굴 탐지
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        #눈 탐지
        eyes = eye_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))

        for(ex, ey, ew, eh) in eyes: #튜플 형태
            cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow('eyes', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""
#"""
import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt') #YOLO 모델, v8,n: nano 버전

image  = cv2.imread('./1216/test.jpg')

#----------------------
from torchvision import datasets

dir(datasets)
#------------------

# #객체 탐지
# results = model.predict(source='./1216/test.jpg', save=False, save_txt=False, conf=0.5) #conf는 신뢰도, 이미지 자체의 경로를 써도 된다

# #결과 시각화
# frame = results[0].plot() #plot(): 탐지된 객체를 시각화한 이미지를 반환

# cv2.imshow('YOLO', frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows() #ModuleNotFoundError: No module named 'torchvision.datasets.caltech'????
#"""

"""
#--------------ocr

import cv2
import pytesseract

#Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

image = cv2.imread('./1216/receipt.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray_image, lang = 'kor')

print('추출된 이미지: ', text)

"""
"""
import cv2
import pytesseract

#Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

image = cv2.imread('./1216/car_number.jpg') #이미지가 번호판 이외의 배경까지 글자로 인식하려다 보니 게속 오류가 뜬 것, ROI 설정해야

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#블러 적용
blur = cv2.GaussianBlur(gray_image, (5, 5), 0)

#_, binary_img = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)

# adaptiveThreshold(): 조명에 대응이 쉽다
binary_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

text = pytesseract.image_to_string(binary_img, lang = 'kor', config = "--psm 7")

print('추출된 이미지: ', text)
"""

