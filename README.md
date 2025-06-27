# Adaptive-AI-SIEM-for-Cyber-Threats


This repository contains the implementation of a smart **AI-powered Security Information and Event Management (SIEM)** system designed to detect and respond to evolving cyber threats. It leverages a **hybrid CNN + LSTM model** for log classification and integrates **Federated Learning** to train models across decentralized datasets securely and privately.

---

## 📑 Table of Contents

- [🧠 Introduction](#introduction)
- [⚙️ Installation](#installation)
- [🗂 Dataset](#dataset)
- [🧼 Preprocessing](#preprocessing)
- [🏗 Model Architecture](#model-architecture)
- [🌐 Federated Learning Simulation](#federated-learning-simulation)
- [💻 Web Interface (Django)](#web-interface-django)
- [🧪 Testing the Model](#testing-the-model)
- [📋 Threat Logging](#threat-logging)
- [📈 Results](#results)
- [🤝 Contributing](#contributing)
- [📄 License](#license)

---

## 🧠 Introduction

This project is a prototype for an **adaptive, intelligent SIEM system** that supports:

- Log-based threat classification using a **hybrid CNN + LSTM** deep learning model
- Text vectorization using **TF-IDF**
- Simulated **Federated Learning** to preserve data locality across clients
- A **Django-based web interface** for real-time predictions and admin training

### 🛠 Built With

- **TensorFlow 2.x**
- **Scikit-learn**
- **Pandas / NumPy**
- **Django 3.x**
- **MySQL**
- **HTML/CSS**

---

## ⚙️ Installation

To set up the project and its dependencies:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/adaptive-ai-siem.git
cd adaptive-ai-siem
````

### 2. Create a Virtual Environment & Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Set Up the MySQL Database

* Create a MySQL database named `cyber_threat`
* Update your `backend/cyber_threat/settings.py` with the correct database credentials

### 4. Run Migrations & Launch the Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🗂 Dataset

Place your dataset in the `datasets/` folder.

* **`raw_event_logs.csv`** — Should contain:

  * `log_content` (string): the security log message
  * `threat_label` (categorical): one of **Benign**, **Anomaly**, or **Attack**

> ⚠️ Ensure your CSV is clean and encoded in UTF-8.

---

## 🧼 Preprocessing

Preprocessing transforms raw log data into a numerical format using **TF-IDF**.

```bash
python ml/preprocessing.py
```

This generates:

* `cyber_event_profiles.csv`: Processed log dataset
* `tfidf_vectorizer.pkl`: Serialized vectorizer for inference

---

## 🏗 Model Architecture

The model architecture uses a combination of **CNN** and **LSTM**:

* 🧩 **TF-IDF**: Converts log content into numerical features
* 🧠 **CNN Layer**: Extracts local temporal patterns
* 🔁 **LSTM Layer**: Learns sequential relationships in logs
* 🎯 **Dense Softmax Output**: Predicts one of three classes

To train the model manually:

```bash
python ml/model_cnn_lstm.py
```

Or via admin panel:

```bash
http://127.0.0.1:8000/train_model/
```

---

## 🌐 Federated Learning Simulation

Federated Learning allows distributed training without centralizing raw data.

### 1. Simulate Client-Side Training

```bash
python ml/federated_client.py
```

### 2. Perform Server-Side Aggregation

```bash
python ml/federated_aggregator.py
```

Or use the web endpoint:

```
http://127.0.0.1:8000/federated_aggregation/
```

Client models are saved as:
`datasets/client_model_1.h5`, `client_model_2.h5`, etc.

---

## 💻 Web Interface (Django)

Access the prediction form at:

```bash
http://127.0.0.1:8000/Predict_CyberThreat_Type/
```

### Supported Views:

* `Predict_CyberThreat_Type/` — User log prediction
* `train_model/` — Trigger training on processed TF-IDF data
* `federated_aggregation/` — Simulate server-side model merging

### Templates Used:

* `Predict_Form.html`
* `Predict_Result.html`

---

## 🧪 Testing the Model

The Django view `Predict_CyberThreat_Type`:

* Loads the `tfidf_vectorizer.pkl` and trained `.h5` model
* Transforms user input
* Predicts class using `model.predict()`

### Sample Inference Code:

```python
tfidf_vector = tfidf.transform([log_input]).toarray().reshape(1, 100, 1)
prediction = model.predict(tfidf_vector)
result = labels[np.argmax(prediction)]
```

---

## 📋 Threat Logging

Each prediction is logged for auditing:

```python
# utils/logger.py
log_threat(input_data, result)
```

Logs are stored at:

```
logs/threat_logs.log
```

Each log entry includes a timestamp, log text, and predicted label.

---

## 📈 Results

Performance metrics can be visualized using:

* 🟢 Accuracy vs Loss plots
* 🔵 Confusion Matrix
* 🟡 Precision / Recall / F1-Score

Use `TensorBoard` or `matplotlib` to enhance visual feedback.

---

## 🤝 Contributing

We welcome community contributions!

### Contribution Guide

1. 🍴 Fork this repository
2. 🌿 Create a new branch (`feature/your-feature`)
3. 💾 Commit your changes
4. 🚀 Push and open a pull request

Your suggestions are appreciated to improve this system.
