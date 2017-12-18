import drum_data_v1 as drum_data
import os.path
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.externals import joblib
import serial
import pyautogui
import time

prev_state = 0
ser = serial.Serial('/dev/ttyUSB0', 115200)

keys = [[0], [1, 4], [2, 3]]

def in_same_group(pred, prev_state):
    for k in keys:
        if pred in k and prev_state in k:
            return True
    return False

def read():
    sensors_read = [int(x) for x in ser.readline().decode().strip().split(',')]
    pred = clf.predict([sensors_read])[0]
    return pred

if not os.path.isfile('drum_model.pkl'):
    clf = svm.SVC(C=100, gamma=0.0001)
    clf.fit(drum_data.features, drum_data.labels)
    joblib.dump(clf, 'drum_model.pkl')
    input("Trained model. Press Enter to start.")
else:
    clf = joblib.load('drum_model.pkl')
    input("Loaded model. Press Enter to start.")

while True:
    try:
        pred = read()
        if not in_same_group(pred, prev_state):
            print(pred)
            prev_state = pred
            if pred == 1:
                pyautogui.keyDown('z')
                time.sleep(0.0001)
                pyautogui.keyUp('z')
            elif pred == 2:
                pyautogui.keyDown('x')
                time.sleep(0.0001)
                pyautogui.keyUp('x')
            elif pred == 3:
                pyautogui.keyDown('c')
                time.sleep(0.0001)
                pyautogui.keyUp('c')
            elif pred == 4:
                pyautogui.keyDown('v')
                time.sleep(0.0001)
                pyautogui.keyUp('v')
    except:
        pass
