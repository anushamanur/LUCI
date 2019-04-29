 from __future__ import print_function
import numpy as np
from keras.models import Sequential
from keras.layers import Dense 


# load json and create model
json_file = open('model1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model1.h5")
print("Loaded model from disk")



arr=[]


PIK1 = "pix_test.dat"


print ("Loading pix data")
with open(PIK1, "rb") as f:
    arr= pickle.load(f)
print ("Completed loading pix data")

x_test=np.array(arr)
print (x_test.shape)  	#(16,4)

''' 
# evaluate loaded model on test data
loaded_model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])
score = loaded_model.evaluate(X, Y, verbose=0)
#print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
print (score)
print (model.metrics_names)
print ("----------------------------------------------")
'''

# calculate predictions
predictions = loaded_model.predict(x_test)
print (predictions)
#print (y_test)
