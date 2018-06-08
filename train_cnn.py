# Gerekli kutuphaneler
from __future__ import print_function

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.optimizers import RMSprop
import numpy
from keras.models import load_model
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

#Oluşturulacak YSA'nın özellikleri.
batch_sayisi = 128
sinif_sayisi = 10
max_epoch_sayisi = 20

# Veri setinin özelliklerinin girilmesi ve hafızaya yüklenmesi
# giriş resminin özellikleri
img_uzunluk, img_genislik = 28, 28

# egitim ve test olarak bolumlendirilmis veri
(x_egitim, y_egitim), (x_test, y_test) = mnist.load_data()

if K.image_data_format() == 'channels_first':
    x_egitim = x_egitim.reshape(x_egitim.shape[0], 1, img_uzunluk, img_genislik)
    x_test = x_test.reshape(x_test.shape[0], 1, img_uzunluk, img_genislik)
    input_shape = (1, img_uzunluk, img_genislik)
else:
    x_egitim = x_egitim.reshape(x_egitim.shape[0], img_uzunluk, img_genislik, 1)
    x_test = x_test.reshape(x_test.shape[0], img_uzunluk, img_genislik, 1)
    input_shape = (img_uzunluk, img_genislik, 1)
    
x_egitim = x_egitim.astype('float32')
x_test = x_test.astype('float32')
x_egitim /= 255
x_test /= 255
print('x_egitim boyutlari:', x_egitim.shape)
print(x_egitim.shape[0], 'egitim verisi')
print(x_test.shape[0], 'test verisi')

# convert class vectors to binary class matrices
y_egitim = keras.utils.to_categorical(y_egitim, sinif_sayisi)
y_test = keras.utils.to_categorical(y_test, sinif_sayisi)

# Modelin olusturulmasi
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(sinif_sayisi, activation='softmax'))

model.summary() # modelin ozetini goster

model.compile(loss=keras.losses.categorical_crossentropy,
                optimizer=keras.optimizers.Adadelta(),
                metrics=['accuracy'])

model.fit(x_egitim, y_egitim,
          batch_size=batch_sayisi,
          epochs=max_epoch_sayisi,
          verbose=1,
          validation_data=(x_test, y_test))
skor = model.evaluate(x_test, y_test, verbose=0)
print('Test kaybi:', skor[0])
print('Test dogrulugu:', skor[1])

model.save("model_cnn.h5") # modelin diske kaydedilmesi
