
from django.http import HttpResponse
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from tensorflow.keras.models import load_model

def train_model(request):
    data = pd.read_csv("cyber_event_profiles.csv")
    X = data.drop('label', axis=1).values.reshape(-1, 100, 1)
    y = to_categorical(LabelEncoder().fit_transform(data['label']))

    model.fit(X, y, epochs=10, batch_size=32)
    model.save('trained_model.h5')
    return HttpResponse("Model Trained and Saved Successfully")
