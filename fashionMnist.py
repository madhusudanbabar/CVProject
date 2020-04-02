# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:34:13 2020

@author: krypton
"""


#%%
from keras.datasets import fashion_mnist
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
import matplotlib.pyplot as plt

X_train = X_train / X_train.max()
X_test = X_test / X_test.max()

#%% 
X_test = X_test.reshape(10000,28,28,1)
X_train = X_train.reshape(60000,28,28,1)

#%% 
from keras.utils.np_utils import to_categorical
y_cat_train = to_categorical(y_train, 10)
y_cat_test = to_categorical(y_test, 10)

#%%
from keras.models import Sequential
from keras.layers import MaxPooling2D, Conv2D, Flatten, Dense

#%% 
model = Sequential()

model.add(Conv2D(filters=32, kernel_size=(4,4), input_shape=(28,28,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
model.summary()
model.fit(X_train, y_cat_train, epochs=10)

#%% 
from sklearn.metrics import classification_report
predicitons = model.predict_classes(X_test)
print(classification_report(y_test, predicitons))

#%% 
model.save("KMnist.h5")
model.evaluate(X_test, y_cat_test)
