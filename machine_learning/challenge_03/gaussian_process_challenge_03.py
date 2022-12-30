import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, RationalQuadratic, Matern, DotProduct

# Resources: https://machinelearningmastery.com/gaussian-processes-for-classification-with-python/
problem = 3
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

from sklearn.model_selection import train_test_split, LeaveOneOut, GridSearchCV

X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(x_train, y_train, test_size=0.4,
                                                                            random_state=42)

# model is your classifier (any object with a fit and predict method)
from sklearn.gaussian_process import GaussianProcessClassifier

model = GaussianProcessClassifier(1 * DotProduct(sigma_0=1))

model.fit(X_train_split, y_train_split)
# model.fit(x_train, y_train)
y_hat = model.predict(X_test_split)
# y_hat = model.predict(x_test)
from sklearn.metrics import accuracy_score

print("Accuraccy score is: ", accuracy_score(y_test_split, y_hat))


submission_file = f'{problem_name}_submission.npz'
np.savez(submission_file, y_test=y_hat)
# Then upload the submission npz to Web-CAT.


grid = dict()
grid['kernel'] = [1 * RBF(), 1 * DotProduct(), 1 * Matern(), 1 * RationalQuadratic(), 1 * WhiteKernel()]
search = GridSearchCV(model, grid, scoring='accuracy', n_jobs=-1)
results = search.fit(X_train_split, y_train_split)
print('Best Mean Accuracy: %.3f' % results.best_score_)
print('Best Config: %s' % results.best_params_)

# summarize all
means = results.cv_results_['mean_test_score']
params = results.cv_results_['params']
for mean, param in zip(means, params):
    print(">%.3f with: %r" % (mean, param))
