import os
from mlxtend.data import loadlocal_mnist
import matplotlib.pyplot as plt
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt
x_train, y_train = loadlocal_mnist(
        images_path='C:\\Users\\ACER\\Downloads\\train-images.idx3-ubyte', 
        labels_path='C:\\Users\\ACER\\Downloads\\train-labels.idx1-ubyte')
x_test, y_test =loadlocal_mnist(images_path='C:\\Users\\ACER\\Downloads\\t10k-images.idx3-ubyte', 
        labels_path='C:\\Users\\ACER\\Downloads\\t10k-labels.idx1-ubyte')
#x_train=x_train[0:20000]
#y_train=y_train[0.20000]
x_train=x_train/255               #mean normalization is very important without which accuracy was very less
x_test=x_test/255
y_test = keras.utils.to_categorical(y_test, num_classes=10)
y_train= keras.utils.to_categorical(y_train, num_classes=10)
model=Sequential()
model= Sequential()
model.add(Dense(32,activation='relu',input_dim=784))
model.add(Dense(10,activation='softmax'))
model.compile(optimizer='SGD',loss='binary_crossentropy',metrics=['accuracy'])
checkpoint = ModelCheckpoint(filepath, monitor='acc', verbose=1, save_best_only=True, mode='max')  ##Model Checkpoints
callbacks_list = [checkpoint]
model.fit(x_train,y_train,batch_size=32,epochs=5,callbacks=callbacks_list)   #can give validation_data=(valid_features, valid_labels)
score=model.evaluate(x_test,y_test,verbose=0)

print('The Accuracy on test data is'+ str(score[1]))

#Prediction

b=x_train[1000]
c=np.resize(b,(28,28))
a=np.resize(b,(1,784))
x=model.predict(a)
maxi=x.max()
x=np.resize(x,(10,))
for i in range(0,10):
    if(x[i]==maxi):
        index=i
        break;
print(index);
plt.imshow(c)       
    
