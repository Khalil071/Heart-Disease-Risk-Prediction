import pickle
import numpy as np
from flask import Flask, request, jsonify

# تحميل النموذج
with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)  # Debugging print

        feature_list = [
        "Age", "Pain_Arms_Jaw_Back", "Cold_Sweats_Nausea", "Dizziness", 
        "Chest_Pain", "Fatigue", "Swelling", "Shortness_of_Breath", "Palpitations",
        "High_Cholesterol", "Sedentary_Lifestyle", "High_BP", "Chronic_Stress",
        "Obesity", "Smoking", "Family_History", "Diabetes", "Gender"]

        # Ensure all features are provided
        missing_features = [feat for feat in feature_list if feat not in data]
        if missing_features:
            return jsonify({'error': f'Missing features: {missing_features}'}), 400

        features = np.array([data[feat] for feat in feature_list]).reshape(1, -1)
        print("Input shape:", features.shape)  # Debugging print

        prediction = rf_model.predict(features)

        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 500