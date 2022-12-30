import numpy as np
import matplotlib.pyplot as plt

problem = 1
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

from sklearn.model_selection import train_test_split, LeaveOneOut

X_train, X_test, y_train_new, y_test = train_test_split(x_train, y_train, test_size=0.4, random_state=42)

# model is your classifier (any object with a fit and predict method)
# from sklearn.model_selection import G
from sklearn.mixture import GaussianMixture as GMM

gmm = GMM(n_components=16, covariance_type='full')
gmm.fit(X_train, y_train_new)
y_hat = gmm.predict(X_test)

from sklearn.metrics import accuracy_score

print("Accuraccy score is: ", accuracy_score(y_test, y_hat))

# Visualising the decision boundaries

from matplotlib.patches import Ellipse

# NOT currently working, possible tweaking will solve...
# def draw_ellipse(position, covariance, ax=None, **kwargs):
#     ax = ax or plt.gca()
#     #     Convert covariancec to principal axes
#     if covariance.shape == (2.2):
#         U, s, vt = np.linalg.svd(covariance)
#         angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
#         width, height = 2 * np.sqrt(s)
#     else:
#         angle = 0
#         width, height = 2 * np.sqrt(covariance)
#
#     #     Draw the ellipse
#     for nsig in range(1, 4):
#         ax.add_patch(Ellipse(position, nsig * width, nsig * height, angle, **kwargs))
#
#
# def plot_gmm(gmm, X, label=True, ax=None):
#     ax = ax or plt.gca()
#     labels = gmm.fit(X).predict(X)
#     if label:
#         ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis', zorder=2)
#     else:
#         ax.scatter(X[:, 0], X[:, 1], s=40, zorder=2)
#     ax.axis('equal')
#
#     w_factor = 0.2 / gmm.weights_.max()
#     for pos, covar, w in zip(gmm.means_, gmm.covariances_, gmm.weights_):
#         draw_ellipse(pos, covar, alpha=w * w_factor)
#
# plot_gmm(gmm, X_train)
# submission_file = f'{problem_name}_submission.npz'
# np.savez(submission_file, y_test=y_hat)
# Then upload the submission npz to Web-CAT.
