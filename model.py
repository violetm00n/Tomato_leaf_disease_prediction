model=Model(inputs=I.input,outputs=Dense(l,activation='softmax')(x))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.fit_generator(tr,validation_data=ts,epochs=10,steps_per_epoch=len(tr),validation_steps=len(ts),callbacks=[callbacks])
model.save('tomatoo.h5')
from google.colab import files
files.download('tomatoo.h5')
