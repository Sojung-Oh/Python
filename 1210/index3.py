import seaborn as sns
import matplotlib.pyplot as plt

# penguins = sns.load_dataset("penguins")

# #print(penguins.head())

# #1-1
# sns.barplot(x = 'species', y = 'body_mass_g', data = penguins)
# plt.show()

# #1-2
# sns.scatterplot(x = 'bill_length_mm', y = 'bill_depth_mm', data = penguins, hue = 'species')
# plt.show()

# #1-3
# sns.violinplot(x = 'island', y = 'body_mass_g', data = penguins)
# plt.show()

#---------------------------------------------------------------------


flights = sns.load_dataset('flights')
print(flights.head())

#연도별 평균값
#avg = flights.groupby('year')['passengers'].mean().reset_index()
#reset_index() : 인덱스를 초기화, 기존 인덱스를 데이터 프레임의 열로 변환

#2-1
#plt.plot(avg['year'], avg['passengers'])
#plt.grid(True)

#print(avg)

#2-2
# pivot = flights.pivot(index = "month", columns = 'year', values= 'passengers')
# print(pivot)
# sns.heatmap(pivot, annot = True, fmt = 'd')

# plt.show()

#2-3
# y_1958 = flights[flights['year'] == 1958]
# sns.barplot(x = 'month', y = 'passengers', data = y_1958)
# plt.show()

#----------------------------------------------------
#실습3

titanic = sns.load_dataset('titanic')
print(titanic.head())
#3-1
#sns.catplot(x = 'class', hue = 'survived', data = titanic, kind = 'count')
#plt.show()

#3-2
sns.kdeplot(data = titanic, x = 'age', hue = 'survived', fill = True)
plt.show()

