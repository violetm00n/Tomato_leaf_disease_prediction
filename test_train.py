train_gen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_gen=ImageDataGenerator(rescale=1./255)
tr=train_gen.flow_from_directory('/content/drive/MyDrive/Crop desease/Tomato/Train',target_size=(224,224),batch_size=16,class_mode='categorical')
ts=test_gen.flow_from_directory('/content/drive/MyDrive/Crop desease/Tomato/Test',target_size=(224,224),batch_size=16,class_mode='categorical')
