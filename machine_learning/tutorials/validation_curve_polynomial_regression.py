# Let’s look at an example of using cross-validation to compute the validation curve for a class of models. Here we
# will use a polynomial regression model: this is a generalized linear model in which the degree of the polynomial is
# a tunable parameter. For example, a degree-1 polynomial fits a straight line to the data; for model parameters and
#
# :
#
# A degree-3 polynomial fits a cubic curve to the data; for model parameters
#
# :
#
# We can generalize this to any number of polynomial features. In Scikit-Learn, we can implement this with a simple
# linear regression combined with the polynomial preprocessor. We will use a pipeline to string these operations
# together (we will discuss polynomial features and pipelines more fully in “Feature Engineering”):

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline


def PolynomalRegression(degree=2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree), LinearRegression(**kwargs))


import numpy as np


def make_data(N, err=1.0, rseed=1):
    # Randomly sample the data
    rng = np.random.RandomState(rseed)
    X = rng.rand(N, 1) ** 2
    y = 10 - 1. / (X.ravel() + 0.1)
    if err > 0:
        y += err * rng.randn(N)
    return X, y


X, y = make_data(40)

import matplotlib.pyplot as plt
import seaborn

seaborn.set()

X_test = np.linspace(-0.1, 1.1, 500)[:, None]
plt.scatter(X.ravel(), y, color='black')
axis = plt.axis()
for degree in [1, 3, 5]:
    y_test = PolynomalRegression(degree).fit(X, y).predict(X_test)
    plt.plot(X_test.ravel(), y_test, label='degree={0}'.format(degree))

plt.xlim(-0.1, 1.0)
plt.ylim(-2, 12)
plt.legend(loc='best')

# We can visualise the validation curve for this data and model
plt.clf()
from sklearn.model_selection import validation_curve

degree = np.arange(0, 21)
train_score, val_score = validation_curve(PolynomalRegression(), X, y, param_name='polynomialfeatures__degree',
                                          param_range=degree, cv=7)
plt.plot(degree, np.median(train_score, 1), color='blue', label='training score')
plt.plot(degree, np.median(val_score, 1), color='red', label='validation score')
plt.legend(loc='best')
plt.ylim(0, 1)
plt.xlabel('degree')
plt.ylabel('score')
# From the above we have determined the optimal polynomial is roughly 3, below we apply
plt.clf()
plt.scatter(X.ravel(), y)
lim = plt.axis()
y_test = PolynomalRegression(3).fit(X, y).predict(X_test)
plt.plot(X_test.ravel(), y_test)
plt.axis(lim)

plt.clf()

X2, y2 = make_data(200)

plt.scatter(X2.ravel(), y2)

degree = np.arange(21)
train_score2, val_score2 = validation_curve(PolynomalRegression(), X2, y2, param_name='polynomialfeatures__degree',
                                            param_range=degree, cv=7)

plt.plot(degree, np.median(train_score2, 1), color='blue', label='training score')
plt.plot(degree, np.median(val_score2, 1), color='red', label='validation score')
plt.plot(degree, np.median(train_score, 1), color='blue', alpha=0.3, linestyle='dashed')
plt.plot(degree, np.median(val_score, 1), color='red', alpha=0.3, linestyle='dashed')
plt.legend(loc='lower center')
plt.ylim(0, 1)
plt.xlabel('degree')
plt.ylabel('score')

# The general behavior we would expect from a learning curve is this:
#
# A model of a given complexity will overfit a small dataset: this means the training score will be relatively high,
# while the validation score will be relatively low.
#
# A model of a given complexity will underfit a large dataset: this means that the training score will decrease,
# but the validation score will increase.
#
# A model will never, except by chance, give a better score to the validation set than the training set: this means
# the curves should keep getting closer together but never cross.

plt.clf()

from sklearn.model_selection import learning_curve

fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

for i, degree in enumerate([2, 9]):
    N, train_lc, val_lc, = learning_curve(PolynomalRegression(degree), X, y, cv=7, train_sizes=np.linspace(0.3, 1, 25))

    ax[i].plot(N, np.mean(train_lc, 1), color='blue', label='training score')
    ax[i].plot(N, np.mean(val_lc, 1), color='red', label='validation score')
    ax[i].hlines(np.mean([train_lc[-1]]), N[0], N[-1], color='gray', linestyle='dashed')

    ax[i].set_ylim(0, 1)
    ax[i].set_xlim(N[0], N[-1])
    ax[i].set_xlabel('training size')
    ax[i].set_ylabel('score')
    ax[i].set_title(f'degree = {degree:14}')
    ax[i].legend(loc='best')

# This is a valuable diagnostic, because it gives us a visual depiction of how our model responds to increasing
# training data. In particular, when your learning curve has already converged (i.e., when the training and
# validation curves are already close to each other), adding more training data will not significantly improve the
# fit! This situation is seen in the left panel, with the learning curve for the degree-2 model.

plt.clf()

# GRID SEARCH

# In practice, models generally have more than one knob to turn, and thus plots of validation and learning curves
# change from lines to multidimensional surfaces. In these cases, such visualizations are difficult and we would
# rather simply find the particular model that maximizes the validation score.

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline

param_grid = {'polynomialfeatures__degree': np.arange(21), 'linearregression__fit_intercept': [True, False],
              'linearregression__normalize': [True, False]}
grid = GridSearchCV(PolynomalRegression(), param_grid, cv=7)

import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
grid.fit(X, y)
print(grid.best_params_)

model = grid.best_estimator_

plt.scatter(X.ravel(), y)
lim = plt.axis()
y_test = model.fit(X, y).predict(X_test)
plt.plot(X_test.ravel(), y_test)
plt.axis(lim)
