import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Dropout,Dense,Flatten

#load data
train_data=pd.read_csv('../Data/digit-recognizer/train.csv')
test_data=pd.read_csv('../Data/digit-recognizer/test.csv')

#data prepration
y_train=np.array(train_data.label).reshape(-1,1)
x_train=np.array(train_data.drop('label',axis=1)).reshape(-1,28,28,1)
x_train=x_train/255

#build CNN
model=keras.models.Sequential()

model.add(Conv2D(64,kernel_size=3,activation='relu',input_shape=(28,28,1)))
model.add(MaxPooling2D())
model.add(Dropout(0.4))
model.add(Conv2D(32,kernel_size=3,activation='relu'))
model.add(MaxPooling2D())
model.add(Dropout(0.4))
model.add(Conv2D(16,kernel_size=3,activation='relu'))
model.add(Flatten())
model.add(Dropout(0.4))
model.add(Dense(100,activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#train the model
model.fit(x_train,y_train,epochs=35)

#make predictions
y_pred=model.predict_classes(x_test)

#save predictions
index=np.arange(1,y_pred.shape[0]+1)
pd.DataFrame(np.c_[index,y_pred],columns=['ImageId','Label'])
pd.to_csv(submission.csv)