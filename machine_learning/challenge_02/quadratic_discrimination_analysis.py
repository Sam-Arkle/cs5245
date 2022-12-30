import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
# Resources: https://scikit-learn.org/stable/modules/lda_qda.html
# https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html

problem = 2
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
model = QuadraticDiscriminantAnalysis()
# Split the data for testing
from sklearn.model_selection import train_test_split, LeaveOneOut, GridSearchCV
X_train, X_test, y_train_new, y_test_new = train_test_split(x_train, y_train, test_size=0.4, random_state=42)


model.fit(x_train, y_train)
y_hat = model.predict(x_test)

from sklearn.metrics import accuracy_score
# print("Accuraccy score is: ", accuracy_score(y_test, y_hat))


submission_file = f'{problem_name}_submission.npz'
np.savez(submission_file, y_test=y_hat)
# Then upload the submission npz to Web-CAT.
