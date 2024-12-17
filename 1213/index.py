import cv2
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

#이미지 읽기
image = cv2.imread('./1213/test_image.jpg')

#opencv BGR -> RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # # cv2.imshow('title', image_rgb)
# # # cv2.waitKey(0)
# # # cv2.destroyAllWindows()

# plt.figure(figsize = (10, 5))

#원본
plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title('원본')
plt.axis('off') #이미지에 x축, y축 표시 안되게 끈 것
#plt.show()


#----------------블러링
# #평균 블러
# blurred = cv2.blur(image_rgb,(10,10)) #이미지를 부옇게 처리하는 정도, 보통은 3, 3을 주로 쓴다

# plt.subplot(2, 2, 2)
# plt.imshow(blurred)
# plt.title('평균블러')
# plt.axis('off')

# #가우시안 블러
# gaussian = cv2.GaussianBlur(image_rgb, (5,5), 0)
# plt.subplot(2, 2, 3)
# plt.imshow(gaussian)
# plt.title('가우시안 블러')
# plt.axis('off') #같은 5, 5인데 가우시안 블러가 더 자연스럽게 나온다

# # #미디언 블러
# median = cv2.medianBlur(image_rgb, 5)
# plt.subplot(2, 2, 4)
# plt.imshow(median)
# plt.title('미디언 블러')
# plt.axis('off') 


# #--------------------엣지 강조
# #샤프닝 커널
# kernel = np.array([ [0, -1, 0],
#                    [-1, 7, -1],
#                    [0, -1, 0]])
# #필터 적용
# sharped = cv2.filter2D(median, -1, kernel)

# plt.subplot(2, 2, 2)
# plt.imshow(sharped)
# plt.title('엣지 강조')
# plt. axis('off')

#----------------엣지 검출

# img = cv2.imread('./1213/test_image.jpg', cv2.IMREAD_GRAYSCALE) #그레이 스케일로 읽어들이기

# #sobel
# sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 3) #x 방향 미분
# sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 3) #y 방향 미분
# #CV_32F (32bit)
# #CV_8U (8bit 정수, unsigned 음수는 지우고 다 양수로 바꿔서 0부터 255) #정밀해야 해서 우리는 잘 안 씀

# sobel_combined = cv2.magnitude(sobel_x, sobel_y) # magnitude는 벡터의 절댓값 계산

# #canny
# edges = cv2.Canny(img, 100, 200) #최소값, 최대값

# plt.subplot(2, 2, 4)
# plt.imshow(edges, cmap='gray')
# plt.title('canny')
# plt.axis('off')


# #원본
# plt.subplot(2, 2, 1)
# plt.imshow(img, cmap = 'gray') #cmap 꼭 gray로 넣어줘야!
# plt.title('원본')
# plt.axis('off')

# #sobel , 엣지만 검출한 그림!
# plt.subplot(2, 2, 2)
# plt.imshow(sobel_combined, cmap='gray')
# plt.title('sobel')
# plt.axis('off')

# #laplacian
# laplacian = cv2.Laplacian(img, cv2.CV_64F)
# plt.subplot(2, 2, 3)
# plt.imshow(laplacian, cmap='gray')
# plt.title('laplacian')
# plt.axis('off')

#--------------------컨투어
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #그레이 스케일로 변환

# #이진화 처리
# _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# #안 쓰는 변수는 _로 표시 가능

# #컨투어 감지
# contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #APPROX_SIMPLE 직선만 검출하여 저장한다

# #컨투어를 원본에 그리기
# results_img = image.copy()
# cv2.drawContours(results_img, contours, -1, (0, 255, 0), 2) #-1 모든 컨투어, RGB색상 순서 튜플, 선 두께

# plt.subplot(2, 2, 2)
# plt.imshow(cv2.cvtColor(results_img, cv2.COLOR_BGR2RGB))
# plt.title('컨투어 그리기')
# plt.axis('off')

# #-----------------컨투어 계산
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #그레이 스케일로 변환 
# _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #APPROX_SIMPLE 직선만 검출하여 저장한다
# results_img = image.copy()

# for contour in contours: #여기서는 컨투어 하나씩 오고 나중에 리스트에 넣어줌
    #면적 계산
    #print('면적: ', cv2.contourArea(contour))

    #중심점 계산
    # M = cv2.moments(contour)
    # if M['m00'] != 0: #중심점 계산 (m00 = 면적)
    #     cx = int(M['m10'] / M['m00']) #x 중심
    #     cy = int(M['m01'] / M['m00']) #y 중심

    #     #중심점 표시
    #     cv2.circle(results_img, (cx, cy), 5, (0, 0, 0), -1) #검은색 점 그리기, 원의 좌표, 반지름, 색상, -1일 때 내부 채우기
    # else:
    #     print('컨투어 면적이 0')

#     #둘레 계산
#     print('둘레 : ',cv2.arcLength(contour, True)) #폐곡선 여부

#     cv2.drawContours(results_img, [contour], -1, (0, 255, 0), 2)

# plt.imshow(cv2.cvtColor(results_img, cv2.COLOR_BGR2RGB))

# plt.show()

#------------------웹캠 연결
#cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("D:\내덕질2\녹화_2023_07_25_17_08_28_456.mp4")

# codec = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', codec, 20.0, (640, 480)) #녹화할 때 쓰는 것!

# plt.ion() #인터렉티드 모드 : 코드를 실행하면서 창을 표시
# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         print('프레임을 읽지 못했습니다')
#         break

#     #out.write(frame)    
#     #cv2.imshow('video', frame)
#     #원본
#     original = frame.copy()

#     #가우시안 블러
#     gaussian = cv2.GaussianBlur(frame, (7, 7), 0)

#     plt.subplot(2, 2, 1)
#     plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
#     plt.title('원본')
#     plt.axis('off')

#     plt.subplot(2, 2, 2)
#     plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))
#     plt.title('가우시안 블러')
#     plt.axis('off')

#     plt.pause(0.001) #1밀리초 동안
#     plt.clf() #현재 플롯창에 띄워진 것을 초기화

#     #'q'키로 종료
#     key = cv2.waitKey(1) #키 입력 대기(1ms)

#     if cv2.waitKey(1) & 0xFF == ord('q'): #'q'키가 입력되었는지 확인
#         break

# cap.release()
# #out.release()
# cv2.destroyAllWindows()
# plt.close()

#------------------------------------------------------------
#실습. 손 윤곽선을 감지하고 필터를 추가

#------------------웹캠 연결
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("D:\내덕질2\녹화_2023_07_25_17_08_28_456.mp4") #나는 동영상 경로로 읽기

#손 윤곽선 감지
#그레이스케일 변환

plt.ion() #인터렉티드 모드 : 코드를 실행하면서 창을 표시
while cap.isOpened():
    ret, frame = cap.read()

    #오류 처리 조건

    if not ret:
        print('프레임을 읽지 못했습니다')
        break

    #out.write(frame)    
    #cv2.imshow('video', frame)

    #원본
    original_mv = frame.copy()

    #그레이스케일 변환
    gray_mv = cv2.cvtColor(original_mv, cv2.COLOR_BGR2GRAY) 
    #임계값 이진화 처리
    _, binary = cv2.threshold(gray_mv, 127, 255, cv2.THRESH_BINARY)
    #컨투어 감지, 손 윤곽선 탐지
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #APPROX_SIMPLE 직선만 검출하여 저장한다
    #컨투어 그리기
    contour_mv = frame.copy()
    cv2.drawContours(contour_mv, contours, -1, (0, 255, 0), 2) #-1 모든 컨투어, RGB색상 순서 튜플, 선 두께

    #필터 추가 - 샤프닝 필터를 적용하여 윤곽선 강조

    # #--------------------엣지 강조
    #샤프닝 커널
    copy2 = frame.copy()
    kernel = np.array([ [0, -1, 0],
                     [-1, 7, -1],
                     [0, -1, 0]])
    #필터 적용
    sharped_mv = cv2.filter2D(copy2, -1, kernel)

    #---------------화면 띄우기
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(original_mv, cv2.COLOR_BGR2RGB))
    plt.title('원본')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(contour_mv, cv2.COLOR_BGR2RGB))
    plt.title('윤곽선(컨투어) 감지')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(sharped_mv, cv2.COLOR_BGR2RGB))
    plt.title('샤프닝 필터')
    plt.axis('off')

    plt.pause(0.001) #1밀리초 동안
    plt.clf() #현재 플롯창에 띄워진 것을 초기화

    #'q'키로 종료
    key = cv2.waitKey(1) #키 입력 대기(1ms)

    if cv2.waitKey(1) & 0xFF == ord('q'): #'q'키가 입력되었는지 확인
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
plt.close()