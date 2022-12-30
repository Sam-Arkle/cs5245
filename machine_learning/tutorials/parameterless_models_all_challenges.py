import numpy as np
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

data_list = []
model_score_dict = dict()
for i in range(1, 13):
    problem = i
    problem_name = f'challenge_{problem:02d}'
    train_file = f'{problem_name}.npz'
    data = np.load(train_file)
    data_list.append(data)
    model_score_dict[problem_name] = (0.0, "")
# Which model is being used

names = [
    "AdaBoost",
    "Naive Bayes",
    "QDA",
    "Nearest Neighbour (3)",
    "SVC Linear",
    "SVC radial",
    "Gaussian Process",
    "Decision Tree",
    "Random Forest",
    "MLP, Neural Net"

]

classifiers = [
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1, max_iter=1000),
]

for name, model in zip(names, classifiers):
    print(f"Results for model {model}, {name}")
    j = 1
    for data in data_list:
        x_train = data['x_train']
        y_train = data['y_train']
        x_test = data['x_test']
        # Split the data for testing
        X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(x_train, y_train, test_size=0.4,
                                                                                    random_state=42)
        model.fit(X_train_split, y_train_split)
        y_hat = model.predict(X_test_split)
        score = accuracy_score(y_test_split, y_hat)
        print(f"Accuraccy score for problem {j} is: ", score)
        if model_score_dict[f"challenge_{j:02d}"][0] < score:
            model_score_dict[f"challenge_{j:02d}"] = (score, name)
        j += 1
    print('-----------------------------------------------------------------\n')
for key in model_score_dict:
    print(f"The high score for {key} was {model_score_dict[key][1]} with a score of {model_score_dict[key][0]}")
# model.fit(x_train, y_train)
# y_hat = model.predict(x_test)


# submission_file = f'{problem_name}_submission.npz'
# np.savez(submission_file, y_test=y_hat)
# Then upload the submission npz to Web-CAT.
