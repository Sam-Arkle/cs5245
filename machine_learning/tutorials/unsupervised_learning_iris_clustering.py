# Clustering algorithm attempts to find distinct groups of data without reference to any labels.
# We will use clustering method caleld Gaussian mixture
# A GMM attempts to model the data as a collectoin of Gaussian blobs.
import seaborn as sns
from sklearn import mixture

iris = sns.load_dataset('iris')
X_iris = iris.drop('species', axis=1)
y_iris = iris['species']

model = mixture.GaussianMixture(n_components=3, covariance_type='full')

model.fit(X_iris)

y_gmm = model.predict(X_iris)
iris['cluster'] = y_gmm

sns.lmplot("PCA1", "PCA2", data=iris, hue='species', col='cluster', fit_reg=False)
# Again this code isn't working as it is deprecated... Need to get a better understanding so we can update it

