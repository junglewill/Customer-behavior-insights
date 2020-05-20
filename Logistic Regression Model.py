import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing, linear_model
from sklearn.feature_selection import f_regression
from sklearn.metrics import accuracy_score 

one_hot_data = pd.read_excel('one hot encoding data.xlsx')

# X = feature values, all the columns except the last column
X = one_hot_data.iloc[:, :-1]

# y = target values, last column of the data frame
y = one_hot_data.iloc[:, -1]

# 建立模型
logistic_regr = linear_model.LogisticRegression()
logistic_regr.fit(X, y)

# 印出 p-value
print(f_regression(X, y)[1])

print(logistic_regr.coef_)

# 計算準確率
NtoA_prediction = logistic_regr.predict(X)
accuracy = logistic_regr.score(X, y)
print(accuracy)

new_one_hot_data = one_hot_data

# del new_one_hot_data['BehaviorType_Fav'], new_one_hot_data['BehaviorType_ViewSalePage'],new_one_hot_data['SessionNumber'], new_one_hot_data['SourceType_APP'], new_one_hot_data['SourceType_WEB'], new_one_hot_data['TrafficSourceCategory_Direct']
del new_one_hot_data['SourceType_APP'], new_one_hot_data['SourceType_WEB']

# X = feature values, all the columns except the last column
new_X = new_one_hot_data.iloc[:, :-1]

# y = target values, last column of the data frame
new_y = new_one_hot_data.iloc[:, -1]

# 建立模型
new_logistic_regr = linear_model.LogisticRegression()
new_logistic_regr.fit(new_X, new_y)

# 印出 p-value
print(f_regression(new_X, new_y)[1])

print(new_logistic_regr.coef_)

# 計算準確率
NtoA_prediction = new_logistic_regr.predict(new_X)
new_accuracy = new_logistic_regr.score(new_X, new_y)
print(new_accuracy)
