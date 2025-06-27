
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder

def simulate_client_training(data_path, model_path):
    model = load_model(model_path)
    df = pd.read_csv(data_path)
    X = df.drop('label', axis=1).values.reshape(-1, 100, 1)
    y = to_categorical(LabelEncoder().fit_transform(df['label']))
    
    model.fit(X, y, epochs=2, batch_size=16)
    model.save(model_path)
    print("Client model updated and saved.")
