
import logging
logging.basicConfig(filename='threat_logs.log', level=logging.INFO)

def log_threat(input_log, prediction):
    logging.info(f"Log: {input_log} --> Prediction: {prediction}")
