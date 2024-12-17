import cv2
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False


# kernel = np.array([[0, -1, 0],
#                    [-1, 7, -1],
#                    [0, -1, 0]])


# #-----------------------------------실습 리더님 코드
# #------------------웹캠 연결
# #cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("D:\내덕질2\녹화_2023_07_25_17_08_28_456.mp4") #나는 동영상 경로로 읽기

# if not cap.isOpened(): #예외 처리
#     print('영상이 열리지 않습니다')
#     exit()

# plt.ion() # 인터렉티브 모드 활성화

# while True:
#     ret, frame = cap.read() #ret은 true false 값
#     if not ret:
#         print('프레임을 열수 없습니다')
#         break
    
#     #그레이로 변환
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     #이진화 처리
#     _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

#     #컨투어 감지
#     contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     #컨투어 그리기
#     contour_frame = frame.copy()
#     cv2.drawContours(contour_frame, contours, -1, (0, 255, 0), 2)

#     #샤프닝 필터
#     sharp = cv2.filter2D(contour_frame, -1, kernel)

#     #원본
#     plt.subplot(2, 2, 1)
#     plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#     plt.title('원본')
#     plt.axis('off')

#     #컨투어
#     plt.subplot(2, 2, 2)
#     plt.imshow(cv2.cvtColor(contour_frame, cv2.COLOR_RGB2BGR))
#     plt.title('컨투어')
#     plt.axis('off')

#     #샤프닝 필터
#     plt.subplot(2, 2, 3)
#     plt.imshow(cv2.cvtColor(sharp, cv2.COLOR_RGB2BGR))
#     plt.title('샤프닝')
#     plt.axis('off')

#     plt.pause(0.001)
#     plt.clf()

#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

# #flthtm gowp
# cap.release()
# cv2.destroyAllWindows() 
# plt.ioff() #인터렉티브 모드 종료



kernel = np.array([[0, -1, 0],
                   [-1, 7, -1],
                   [0, -1, 0]])


#-----------------------------------실습 리더님 코드
#------------------웹캠 연결
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("D:\내덕질2\녹화_2023_07_25_17_08_28_456.mp4") #나는 동영상 경로로 읽기

if not cap.isOpened(): #예외 처리
    print('영상이 열리지 않습니다')
    exit()

plt.ion() # 인터렉티브 모드 활성화
fig, axes = plt.subplots(2, 2, figsize = (10, 10))


while True:
    ret, frame = cap.read() #ret은 true false 값
    if not ret:
        print('프레임을 열수 없습니다')
        break
    
    #그레이로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #이진화 처리
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    #컨투어 감지
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #컨투어 그리기
    contour_frame = frame.copy()
    cv2.drawContours(contour_frame, contours, -1, (0, 255, 0), 2)

    #샤프닝 필터
    sharp = cv2.filter2D(contour_frame, -1, kernel)

    #원본

    axes[0,0].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    axes[0,0].set_title('원본')
    axes[0,0].axis('off')

    #컨투어
    
    axes[0,1].imshow(cv2.cvtColor(contour_frame, cv2.COLOR_RGB2BGR))
    axes[0,1].set_title('컨투어')
    axes[0,1].axis('off')

    #샤프닝 필터
    axes[1,0].imshow(cv2.cvtColor(sharp, cv2.COLOR_RGB2BGR))
    axes[1,0].set_title('샤프닝')
    axes[1,0].axis('off')

    plt.pause(0.001)
    plt.clf()

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

#flthtm gowp
cap.release()
cv2.destroyAllWindows() 
plt.ioff() #인터렉티브 모드 종료