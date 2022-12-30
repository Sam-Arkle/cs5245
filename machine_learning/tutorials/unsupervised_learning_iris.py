# Looking at reducing dimensionality
# Is there a suitable lower dimensional representation that retians the essntial features of the data?
# Will use principal component analysis

from sklearn.decomposition import PCA
import seaborn as sns

iris = sns.load_dataset('iris')
X_iris = iris.drop('species', axis=1)
y_iris = iris['species']

model = PCA(n_components=2)
model.fit(X_iris)
X_2D = model.transform(X_iris)

iris['PCA1'] = X_2D[:, 0]
iris['PCA2'] = X_2D[:, 1]

sns.lmplot(data=iris,x="PCA1", y="PCA2", hue='species', fit_reg=False)

# Code not working annoyingly. Should look for an updated version online...