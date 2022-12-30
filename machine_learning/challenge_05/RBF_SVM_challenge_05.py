import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

problem = 5
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
model = SVC(C=1, gamma=2)
# Split the data for testing
from sklearn.model_selection import train_test_split, LeaveOneOut, GridSearchCV

X_train, X_test, y_train_new, y_test = train_test_split(x_train, y_train, test_size=0.4, random_state=42)
from sklearn.model_selection import GridSearchCV

# defining parameter range
param_grid = {'C': [0.1, 0.2, 0.3, 0.4, 0.5],
              'gamma': [1, 2, 3, 4, 5],
              'kernel': ['rbf']}

grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=3)

# fitting the model for grid search
grid.fit(X_train, y_train_new)
# print best parameter after tuning
print(grid.best_params_)

# print how our model looks after hyper-parameter tuning
print(grid.best_estimator_)
grid_predictions = grid.predict(X_test)

# print classification report
from sklearn.metrics import accuracy_score, classification_report
print(classification_report(y_test, grid_predictions))

model.fit(x_train, y_train)
y_hat = model.predict(x_test)


# print("Accuraccy score is: ", accuracy_score(y_test, y_hat))

submission_file = f'{problem_name}_submission.npz'
np.savez(submission_file, y_test=y_hat)
# Then upload the submission npz to Web-CAT.
