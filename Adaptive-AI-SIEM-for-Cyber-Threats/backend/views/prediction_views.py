
import numpy as np
from django.shortcuts import render
from tensorflow.keras.models import load_model
from .tfidf_loader import tfidf  # assuming you saved the vectorizer separately
from utils.logger import log_threat

model = load_model('trained_model.h5')

def Predict_CyberThreat_Type(request):
    if request.method == "POST":
        input_data = request.POST['log_text']
        tfidf_vector = tfidf.transform([input_data]).toarray().reshape(1, 100, 1)
        prediction = model.predict(tfidf_vector)
        label = np.argmax(prediction)
        labels = {0: "Benign", 1: "Anomaly", 2: "Attack"}
        result = labels[label]
        log_threat(input_data, result)
        return render(request, 'Predict_Result.html', {'result': result})
    return render(request, 'Predict_Form.html')
