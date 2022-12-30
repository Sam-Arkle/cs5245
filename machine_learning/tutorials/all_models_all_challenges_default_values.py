import numpy as np
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

data_list = []
for i in range(1, 13):
    problem = i
    problem_name = f'challenge_{problem:02d}'
    train_file = f'{problem_name}.npz'
    data = np.load(train_file)
    data_list.append(data)
# Which model is being used

names = [
    "AdaBoost",
    "Naive Bayes",
    "QDA",
]

classifiers = [
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),


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
        print(f"Accuraccy score for problem {j} is: ", accuracy_score(y_test_split, y_hat))
        j += 1
    print('-----------------------------------------------------------------\n')

# model.fit(x_train, y_train)
# y_hat = model.predict(x_test)


# submission_file = f'{problem_name}_submission.npz'
# np.savez(submission_file, y_test=y_hat)
# Then upload the submission npz to Web-CAT.
