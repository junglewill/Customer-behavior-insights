from sklearn import datasets, ensemble, metrics, tree

x_train, x_test, y_train, y_test=train_test_split(pd.concat([dead_x, rise_x]), pd.concat([dead_y, rise_y])[["results"]],test_size=0.2, random_state=0)

clf = tree.DecisionTreeClassifier()
clf.fit(x_train, y_train.values)

error=0
for i, v in enumerate(clf.predict(x_test)):
    if v!= y_test.values[i]:
        error=error+1
print(error)
print(len(clf.predict(x_test)))
