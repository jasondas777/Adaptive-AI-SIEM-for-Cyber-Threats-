
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv1D, MaxPooling1D, LSTM, Dense, Dropout, Reshape

input_layer = Input(shape=(100, 1))
x = Conv1D(64, 3, activation='relu')(input_layer)
x = MaxPooling1D(2)(x)
x = Dropout(0.3)(x)
x = Reshape((x.shape[1], x.shape[2]))(x)
x = LSTM(64)(x)
x = Dropout(0.3)(x)
x = Dense(64, activation='relu')(x)
output = Dense(3, activation='softmax')(x)

model = Model(inputs=input_layer, outputs=output)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
