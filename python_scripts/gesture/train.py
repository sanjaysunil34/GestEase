# Automate gestease_keypoint_training.ipynb

# import nbformat
# from nbconvert.preprocessors import ExecutePreprocessor
# ep = ExecutePreprocessor()
# with open('./gestease_keypoint_training.ipynb') as notebook_file:
#     nb = nbformat.read(notebook_file, as_version=4)
#     ep.preprocess(nb)

# --------------------------------------------------------------------------------

import csv

import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import os

import matplotlib.pyplot as plt

RANDOM_SEED = 42

dirname = os.path.dirname(__file__)
dataset = os.path.join(dirname, 'model/keypoint_classifier/keypoint.csv')
model_save_path = os.path.join(dirname,'model/keypoint_classifier/keypoint_classifier.hdf5')
tflite_save_path = os.path.join(dirname,'model/keypoint_classifier/keypoint_classifier.tflite')

import os
from keypoint_csv_from_video import dirname

csv_path_keypoint = os.path.join(dirname, 'model/keypoint_classifier/keypoint.csv')
with open(csv_path_keypoint, "r") as scraped:
        NUM_CLASSES = int(scraped.readlines()[-1].split(',')[0])+1

X_dataset = np.loadtxt(dataset, delimiter=',', dtype='float32', usecols=list(range(1, (21 * 2) + 1)))
y_dataset = np.loadtxt(dataset, delimiter=',', dtype='int32', usecols=(0))
X_train, X_test, y_train, y_test = train_test_split(X_dataset, y_dataset, train_size=0.75, random_state=RANDOM_SEED)

model = tf.keras.models.Sequential([
    tf.keras.layers.Input((21 * 2, )),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(NUM_CLASSES, activation='softmax')
])

# Model checkpoint callback
cp_callback = tf.keras.callbacks.ModelCheckpoint(model_save_path, verbose=1, save_weights_only=False)
# Callback for early stopping
es_callback = tf.keras.callbacks.EarlyStopping(patience=20, verbose=1)

# Model compilation
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history=model.fit(
    X_train,
    y_train,
    epochs=1000,
    batch_size=128,
    validation_data=(X_test, y_test),
    callbacks=[cp_callback,es_callback]
)



# Save as a model dedicated to inference
model.save(model_save_path, include_optimizer=False)

# Transform model (quantization)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quantized_model = converter.convert()

open(tflite_save_path, 'wb').write(tflite_quantized_model)


