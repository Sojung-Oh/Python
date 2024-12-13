import cv2
import matplotlib.pyplot as plt

#이미지 읽기
image = cv2.imread('./1213/test_image.jpg')

#opencv BGR -> RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # cv2.imshow('title', image_rgb)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

plt.figure(figsize = (10, 5))

#원본
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.axis('off') #이미지에 x축, y축 표시 안되게 끈 것
#plt.show()

#평균 블러
blurred = cv2.blur(image_rgb,(10,10)) #이미지를 부옇게 처리하는 정도, 보통은 3, 3을 주로 쓴다

plt.subplot(1, 2, 2)
plt.imshow(blurred)
plt.axis('off')
plt.show()