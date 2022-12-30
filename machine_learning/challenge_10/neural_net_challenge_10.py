import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
# Resources: https://www.kaggle.com/code/hatone/mlpclassifier-with-gridsearchcv/script#L72
problem = 10
problem_name = f'challenge_{problem:02d}'
train_file = f'{problem_name}.npz'
data = np.load(train_file)
x_train = data['x_train']
y_train = data['y_train']
x_test = data['x_test']
plt.clf()
plt.scatter(x_train[y_train == 0, 0], x_train[y_train == 0, 1], label=r'$y=0$',
            color='blue', marker='*')
plt.scatter(x_train[y_train == 1, 0], x_train[y_train == 1, 1], label=r'$y=1$',
            color='red', marker='+')
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title(f'Data set {problem} train')
plt.legend()
plt.axis('equal')
plt.show()
# model is your classifier (any object with a fit and predict method)
model = MLPClassifier(alpha=1e-09, max_iter=1000)

scaler = StandardScaler()

# Split the data for testing
from sklearn.model_selection import train_test_split, LeaveOneOut, GridSearchCV

X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(x_train, y_train, test_size=0.4,
                                                                            random_state=42)
model.fit(X_train_split, y_train_split)
# model.fit(x_train, y_train)
y_hat = model.predict(X_test_split)
# y_hat = model.predict(x_test)

from sklearn.metrics import accuracy_score

print("Accuraccy score is: ", accuracy_score(y_test_split, y_hat))

# submission_file = f'{problem_name}_submission.npz'
# np.savez(submission_file, y_test=y_hat)
# Then upload the submission npz to Web-CAT.

#
# scaler.fit(X_train_split)
# X_train = scaler.transform(X_train_split)
# X_test = scaler.transform(X_test)


# Grid search for optimal alpha value

# dt = DecisionTreeClassifier()
mlp = MLPClassifier()
from sklearn.model_selection import GridSearchCV

# defining parameter range
parameters = {'solver': ['lbfgs'], 'max_iter': [1000], 'alpha': 10.0 ** -np.arange(1, 10), 'hidden_layer_sizes':np.arange(10, 15), 'random_state':[0,1]}
clf = GridSearchCV(MLPClassifier(), parameters, n_jobs=-1)

# fitting the model for grid search
grid_search = clf.fit(X_train_split, y_train_split)

print(grid_search.best_params_)
accuracy = grid_search.best_score_ *100
print("Accuracy for our training dataset with tuning is : {:.2f}%".format(accuracy) )

