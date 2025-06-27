
from tensorflow.keras.models import load_model
import numpy as np

def average_weights(model_paths):
    models = [load_model(p) for p in model_paths]
    weights = [m.get_weights() for m in models]
    new_weights = []
    for layers in zip(*weights):
        new_weights.append(np.array(layers).mean(axis=0))
    avg_model = models[0]
    avg_model.set_weights(new_weights)
    avg_model.save("aggregated_model.h5")
