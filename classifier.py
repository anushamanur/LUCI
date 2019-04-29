from __future__ import print_function
import numpy as np
#import keras
#import cv2
import pickle
from keras.models import Sequential
from keras.layers import Dense 
#from sklearn.model_selection import train_test_split
import time


arr=[]
label=[]

PIK1 = "pix.dat"
PIK2 = "label.dat"

print ("Loading pix data")
with open(PIK1, "rb") as f:
    arr= pickle.load(f)
print ("Completed loading pix data")

print ("Loading labal data")
with open(PIK2, "rb") as f:
    label= pickle.load(f)
print ("Completed loading label data")
  
#x_train is an numpy array which contains the pixels
x_train=np.array(arr)
print (x_train.shape)  	#(16,4)
print (x_train[0])


y_train=np.array(label)
print (y_train.shape)  	#(16,5)
print (y_train[0])


model = Sequential()
model.add(Dense(32, input_shape=(4,), activation='relu'))
model.add(Dense(5, activation='softmax'))
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

print ("Training has begun")
time1=time.time()
model.fit(x=x_train,y=y_train,validation_split=0.2,epochs=8)
time2=time.time()
print ("Training has ended")

time_for_training=time2-time1
'''with open("time to train","w") as f:
    f.write(time_for_training)'''
# serialize model to JSON
model_json = model.to_json()
with open("model1.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model1.h5")
print("Saved model to disk")

