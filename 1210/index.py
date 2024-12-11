import matplotlib.pyplot as plt
from matplotlib import font_manager
#폰트 경로찾기
# font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
# print(font_list)
path = "Pretendard-Medium.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

#------------------------------------
#히스토그램

# data = [1, 2, 2, 3, 3,3 ,3, 4, 5,5 ,5, 5,5 ,6]
# plt.hist(data, bins = 5, color = "green", histtype="step")

# plt.title("Histogram")
# plt.xlabel("Value")
# plt.ylabel("count")
# plt.show()

#bins = 5 [1,2], [2,3], [3,4], [4,5], [5,6]
#bins = 10 [1, 1.5], [1.5, 2], [2, 2.5]

# #여러 개 data
data1 = [1, 2, 2, 3, 3, 3, 4]
data2 = [2, 3, 3, 4, 4, 5, 6]

plt.hist([data1, data2], bins = 5, color = ["green", "purple"], alpha = 0.5, label = ["data1", "data2"]) #alpha는 투명도

plt.title("Histograms")
plt.xlabel("한글")
plt.ylabel("count")
plt.legend()
plt.show()


#-----------------------------------------
#산점도
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
# sizes = [20, 50, 80, 100, 200]
# colors = [10, 20, 30, 40, 50]


# plt.scatter(x, y,s = sizes, c = colors, cmap = "viridis") #c에 배열을 넣어줬을 때는 cmap 넣어줘야!
# plt.colorbar(label = "Color Bar")

# plt.show()


# import numpy as np

# n = 50
# x = np.random.rand(n)
# y = np.random.rand(n) #0과 1 사이 난수

# #print(x, y)
# area = (30*np.random.rand(n)) ** 2 #0과 30 사이 난수 생성하고 제곱하여 크기 생성
# colors = np.random.rand(n)

# plt.scatter(x, y, s = area, c = colors, cmap="Spectral", alpha = 0.5)

# plt.show()

#-------------------------------------------------------------------------------
#파이 차트
# sizes = [25, 25, 20, 20]
# labels = ["A", "B", "C", "D"]

#강조 파이차트
# sizes = [15, 30, 45, 10]
# labels = ["apple", "banana", "grape", "cherry"]
# explode = [0, 0.1, 0, 0]

# plt.pie(sizes, labels = labels)

# plt.pie(sizes, labels=labels, explode = explode, autopct = "%1.1f%%", shadow = True, startangle=140)

#색상 꾸미기
# sizes = [10, 20, 30, 40]
# labels = ["A", "B", "C", "D"]
# colors = ["gold", "lightblue", "lightgreen", "pink"]

# plt.pie(sizes,labels = labels, colors = colors, autopct="%1.1f%%", textprops = {"fontsize": 15, "color": "darkblue"},
#         wedgeprops={"edgecolor": "black"})

#도넛
# sizes = [40, 30, 20, 10]
# labels = ['X', 'Y', 'Z', 'W']

# plt.pie(sizes, labels = labels, wedgeprops={"width": 0.4})

# plt.show()


#실습1. 그래프 그리기

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# sales_2019 = [100, 120, 140, 110, 130, 150, 160, 170, 180, 200, 190, 210]
# sales_2020 = [90, 110, 130, 120, 140, 160, 170, 160, 150, 180, 200, 190]

# plt.figure(figsize = (10,6)) #그래프 창의 크기
# plt.plot(months, sales_2019, label = "2019", color = "blue", linewidth = 2)
# plt.plot(months, sales_2020, label = "2020", color = "orange", linewidth = 2)

# plt.xlabel("Month", fontsize = 10)
# plt.ylabel("Sales", fontsize = 10)
# plt.title("Monthly Sales Comparison (2019-2020)", fontsize = 15, pad = 10)

# plt.show()

#실습2. 그래프 그리기

# categories = ['Category 1', 'Categoryb2', 'Category 3', 'Category 4', 'Category 5']
# data = [20, 35, 15, 27, 45]

# plt.bar(categories, data, color = 'blue', alpha = 0.7)

# plt.xticks(rotation = 45))
# plt.grid(True, axis = "both", linestyle = "--", alpha = 0.6)

# plt.xlabel("Categories", fontsize = 10)
# plt.ylabel("Values", fontsize = 10)
# plt.title("Bar Chart", fontsize = 15)

# plt.show()

#실습3. 그래프 그리기

# sizes = [18, 16, 32, 34]
# labels = ['Grape', 'Melon', 'Banana', 'Apple']
# explode = [0.1, 0, 0.1, 0]

# #plt.pie(sizes, labels = labels, wedgeprops={"width": 0.4})
# plt.pie(sizes, labels=labels, wedgeprops={"width": 0.7, "edgecolor": 'black'}, explode = explode, autopct = "%1.1f%%", startangle=140)

# plt.show()
