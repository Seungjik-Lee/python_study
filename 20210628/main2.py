import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df = pd.read_csv('https://bit.ly/perch_csv_data')
perch_full = df.to_numpy()
# print(perch_full)

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state=42)
# print(train_input[:5])
# print(train_target[:5])
# print(test_input[:5])
# print(test_target[:5])

poly = PolynomialFeatures()
poly.fit([[2, 3]])
train_poly = poly.transform([[2, 3]])
# print(poly.get_feature_names())
# print(trans_ploy)

poly.fit(train_input)
train_poly = poly.transform(train_input)
# print(poly.get_feature_names())
# print(train_input[:1])
# print(train_input[:1])
# print(train_poly[:5])
test_poly = poly.transform(test_input)

lr = LinearRegression()
lr.fit(train_poly, train_target)
print('훈련데이터를 넣을때 리니어리그레이션 알고리즘 점수')
print(lr.score(train_poly, train_target))
print('테스트데이터를 넣을때 리니어리그레이션 알고리즘 점수')
print(lr.score(test_poly, test_target))

#특성을 변형시킬때 x의 제곱까지지만 특성을 더 많이 변화시키기 위해서 degree 5로 변경
poly = PolynomialFeatures(degree=5, include_bias=False)

poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)
# print(train_poly.shape)
# print(train_poly[0])
# print(poly.get_feature_names())

lr.fit(train_poly, train_target)
print('55개의 특성을 가지고 훈련데이터로 리니어모델을 점수')
print(lr.score(train_poly, train_target))
print('55개의 특성을 가지고 테스트데이터로 리니어모델을 점수')
print(lr.score(test_poly, test_target))