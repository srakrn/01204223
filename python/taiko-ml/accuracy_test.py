import drum_data_v1 as drum_data
import testing_data
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
import numpy
import os.path

if not os.path.isfile('drum_model.pkl'):
    print("No model found. Tuning only parameters.")
else:
    clf = joblib.load('drum_model.pkl')
    print("Loaded model.")

    prediction = clf.predict(testing_data.features)
    acc_score = accuracy_score(prediction, testing_data.labels)
    print("Accuracy Score: {}".format(acc_score))

C = [1, 10, 100, 1000]
gamma = [0.001, 0.0001]

for _c in C:
    for _g in gamma:
        print("C: {}, Gamma: {}".format(_c, _g))
        clf = svm.SVC(C=_c, gamma=_g)
        clf.fit(drum_data.features, drum_data.labels)
        prediction = clf.predict(testing_data.features)
        acc_score = accuracy_score(prediction, testing_data.labels)
        print("\tAccuracy Score: {}".format(acc_score))
