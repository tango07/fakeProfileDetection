import sys
import csv
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

import gender_guesser.detector as gender

from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate

from sklearn import metrics
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.model_selection import learning_curve
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from sklearn.ensemble import RandomForestClassifier


def read_datasets():
    """ Reads users profile from csv files """
    real_users = pd.read_csv("data/users.csv")
    fake_users = pd.read_csv("data/fusers.csv")

    x = pd.concat([real_users, fake_users])
    y = len(fake_users) * [0] + len(real_users) * [1]

    return x, y


def predict_sex(name):
    d = gender.Detector(case_sensitive=False)
    first_name = str(name).split(' ')[0]
    sex = d.get_gender(u"{}".format(first_name))

    sex_code_dict = {'female': -2, 'mostly_female': -1, 'unknown': 0, 'andy': 0, 'mostly_male': 1, 'male': 2}
    code = sex_code_dict[sex]

    return code


def extract_features(x):
    lang_list = list(enumerate(np.unique(x['lang'])))

    lang_dict = {name: i for i, name in lang_list}

    x.loc[:, 'lang_code'] = x['lang'].map(lambda x: lang_dict[x]).astype(int)
    x.loc[:, 'sex_code'] = predict_sex(x['name'])

    feature_columns_to_use = ['statuses_count', 'followers_count', 'friends_count', 'favourites_count', 'listed_count',
                              'sex_code', 'lang_code']
    x = x.loc[:, feature_columns_to_use]

    return x


def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
                        n_jobs=1, train_sizes=np.linspace(.1, 1.0, 5)):
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")

    return plt

def plot_confusion_matrix(cm, title='CONFUSION MATRIX', cmap=plt.cm.Reds):
    target_names=['Fake','Genuine']
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=45)
    plt.yticks(tick_marks, target_names)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def train(X_train, y_train, X_test, nSplits, CV):
    """ Trains and predicts dataset with a SVM classifier """
    # Scaling features
    X_train = preprocessing.scale(X_train)
    X_test = preprocessing.scale(X_test)

    Cs = 10.0 ** np.arange(-2, 3, .5)
    gammas = 10.0 ** np.arange(-2, 3, .5)
    param = [{'gamma': gammas, 'C': Cs}]

    cvk = StratifiedKFold(n_splits=nSplits)

    classifier = SVC()

    clf = GridSearchCV(classifier, param_grid=param, cv=cvk)
    clf.fit(X_train, y_train)

    print("The best classifier is: ", clf.best_estimator_)
    clf.best_estimator_.fit(X_train, y_train)

    print()

    # Estimate score
    scores = cross_validate(clf.best_estimator_, X_train, y_train, cv=CV)

    for k in [*scores]:
        print(k + ": ", scores[k])

    # print()
    #
    # print("Mean Training Score: {}".format(scores['train_score'].mean()))
    # print("Mean Test Score: {}".format(scores['test_score'].mean()))

    title = 'Learning Curves (SVM, rbf kernel, gamma={})'.format(clf.best_estimator_.gamma)

    plot_learning_curve(clf.best_estimator_, title, X_train, y_train, cv=CV)
    plt.show()

    # Predict class
    y_pred = clf.best_estimator_.predict(X_test)

    return y_test, y_pred

x,y = read_datasets()
print("dataset read complete")

x = extract_features(x)
print(x.columns)

# splitting train and test data
X_train,X_test,y_train,y_test = train_test_split(x, y, test_size=0.20, random_state=44)

y_test,y_pred = train(X_train,y_train,X_test,5, 7)

rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
rf_classifier.fit(X_train, y_train)
train_predictions = rf_classifier.predict(X_train)
prediction = rf_classifier.predict(X_test)

print(X_test)
err_training = mean_absolute_error(train_predictions, y_train)
err_test = mean_absolute_error(prediction, y_test)

print("Train Accuracy is : {}".format(100 - (100*err_training)))
print("Test Accuracy is : {}".format(100 - (100*err_test)))


class Predict:
    def prediction(self,l):
        p = rf_classifier.predict(l)

        print(l)
        if p == 0:
            return "REAL"
        if p == 1:
            return "FAKE"
        return "Sorry!, This is beyond my reach..."
