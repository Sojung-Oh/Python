import cv2
import numpy as np

image = cv2.imread("./1216/apple.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([35, 130, 130])
upper = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

count = 0
for con in contours:
    area = cv2.contourArea(con)


    if area > 500: #작은 노이즈 제거
        count += 1
        x, y, w, h = cv2.boundingRect(con) #객체를 감싸는 가장 작은 축에 정렬된 사각형

        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

print(f"검출된 초록색은: {count}개")
cv2.imshow("green", image)
cv2.waitKey(0)
cv2.destroyAllWindows()