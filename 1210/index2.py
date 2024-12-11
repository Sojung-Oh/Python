import seaborn as sns
#print(sns.get_dataset_names())
import matplotlib.pyplot as plt

#예제 데이터
# tips = sns.load_dataset('tips')
# print(tips.head())

# #sns.scatterplot(x = 'total_bill', y = 'tip', hue = 'size', palette = 'deep', style = 'time', size = 'size', data = tips)

# #sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter = True, hue = 'size', dodge = True)
# #sns.swarmplot(x = 'day', y = 'total_bill', data = tips, hue = 'size', dodge = True)

# #sns.relplot(x = 'total_bill', y = 'tip', data = tips, style = 'time', hue = 'sex')
# #sns.catplot(x = 'day', y = 'total_bill', data = tips, hue = 'sex', kind = 'point')
# #sns.displot(tips['total_bill'], bins = 30, kde = True)

# # import numpy as np
# # data = np.random.rand(10,10)
# # sns.heatmap(data, annot = True, fmt = ".2f")

# #sns.pairplot(tips, hue = "sex")
# sns.regplot(x='total_bill', y = 'tip', data = tips)

# plt.show()

#실습1. 데이터 분석 후 그래프 그리기

#펭귄 데이터 셋 불러오기
penguins = sns.load_dataset('penguins')
print(penguins.info())

#펭귄의 종(species)별 평균 몸무게(body_mass_g)를 막대 그래프로 나타내세요.

adelie_data = penguins lambda
#print(adelie_data)