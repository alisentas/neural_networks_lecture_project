# Gerekli kutuphaneler
from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import numpy

# Oluşturulacak YSA'nın özellikleri.
batch_sayisi = 128
sinif_sayisi = 10
max_epoch_sayisi = 20


# giriş resminin özellikleri
img_uzunluk, img_genislik = 28, 28

# Veri setinin özelliklerinin girilmesi ve hafızaya yüklenmesi
# egitim ve test olarak bolumlendirilmis veri
(x_egitim, y_egitim), (x_test, y_test) = mnist.load_data()

x_egitim = x_egitim.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
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

# Modelin oluşturulması
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(sinif_sayisi, activation='softmax'))

model.summary() # modelin ozetini goster

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(), 
              metrics=['accuracy'])
              
history = model.fit(x_egitim, y_egitim,
                    batch_size=batch_sayisi,
                    epochs=max_epoch_sayisi,
                    verbose=1,
                    validation_data=(x_test, y_test))
skor = model.evaluate(x_test, y_test, verbose=0)
print('Test kaybi:', skor[0])
print('Test dogrulugu:', skor[1])

model.save("model_mlp.h5") # Modeli diske kaydetme
