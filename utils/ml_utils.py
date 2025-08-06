# utils/ml_utils.py
import joblib

def load_model(path="D:\AI_Assistant\models\decision_tree_model - Copy.pkl"):
    model = joblib.load(path)
    return model

def predict_next_step(model, features):
    return model.predict([features])[0]
