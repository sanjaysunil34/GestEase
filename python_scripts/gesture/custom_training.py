import numpy as np
from sklearn import svm
import joblib
import os
from sklearn.model_selection import train_test_split

def training():
    RANDOM_SEED = 42
    dirname = os.path.dirname(__file__)
    dataset = os.path.join(dirname, 'model/keypoint_classifier/keypoint.csv')
    model_save_path = os.path.join(dirname,'model/keypoint_classifier/keypoint_classifier.joblib')

    # Set up data
    X_dataset = np.loadtxt(dataset, delimiter=',', dtype='float32', usecols=list(range(1, (21 * 2) + 1)))
    y_dataset = np.loadtxt(dataset, delimiter=',', dtype='int32', usecols=(0))
    X_train, X_test, y_train, y_test = train_test_split(X_dataset, y_dataset, train_size=0.75, random_state=RANDOM_SEED)

    # Create an SVM model with linear kernel
    model = svm.SVC(kernel='linear')

    # Train the model
    model.fit(X_train, y_train)
    # Save the model to a file
    joblib.dump(model, model_save_path)
