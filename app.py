from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Load the trained model and encoders
try:
    model = joblib.load('models/crop_yield_model.pkl')
    area_encoder = joblib.load('models/area_encoder.pkl')
    item_encoder = joblib.load('models/item_encoder.pkl')
    
    # Load unique areas and items
    with open('models/unique_areas.txt', 'r') as f:
        unique_areas = [line.strip() for line in f.readlines()]
    
    with open('models/unique_items.txt', 'r') as f:
        unique_items = [line.strip() for line in f.readlines()]
        
    print("✅ Model and encoders loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None
    area_encoder = None
    item_encoder = None
    unique_areas = []
    unique_items = []

@app.route('/')
def index():
    """Serve the main application page"""
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict_yield():
    """Predict crop yield based on input parameters"""
    try:
        data = request.get_json()
        
        # Extract input parameters
        area = data.get('area', '').lower()
        item = data.get('item', '').lower()
        year = int(data.get('year', 2024))
        rainfall = float(data.get('rainfall', 1000))
        pesticides = float(data.get('pesticides', 100))
        temperature = float(data.get('temperature', 20))
        
        # Validate inputs
        if area not in unique_areas:
            return jsonify({'error': f'Area "{area}" not found. Available areas: {unique_areas[:10]}...'}), 400
        
        if item not in unique_items:
            return jsonify({'error': f'Crop "{item}" not found. Available crops: {unique_items[:10]}...'}), 400
        
        if year < 1990 or year > 2030:
            return jsonify({'error': 'Year must be between 1990 and 2030'}), 400
        
        if rainfall < 0 or rainfall > 5000:
            return jsonify({'error': 'Rainfall must be between 0 and 5000 mm'}), 400
        
        if pesticides < 0 or pesticides > 10000:
            return jsonify({'error': 'Pesticides must be between 0 and 10000 tonnes'}), 400
        
        if temperature < -50 or temperature > 50:
            return jsonify({'error': 'Temperature must be between -50 and 50°C'}), 400
        
        # Encode categorical variables
        area_encoded = area_encoder.transform([area])[0]
        item_encoded = item_encoder.transform([item])[0]
        
        # Create feature array
        features = np.array([[area_encoded, item_encoded, year, rainfall, pesticides, temperature]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Calculate confidence score (simplified)
        confidence = min(95, max(60, 100 - abs(prediction - 50000) / 1000))
        
        # Generate insights
        insights = generate_insights(area, item, year, rainfall, pesticides, temperature, prediction)
        
        return jsonify({
            'prediction': round(prediction, 2),
            'confidence': round(confidence, 1),
            'insights': insights,
            'input_data': {
                'area': area.title(),
                'item': item.title(),
                'year': year,
                'rainfall': rainfall,
                'pesticides': pesticides,
                'temperature': temperature
            }
        })
        
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

@app.route('/api/areas', methods=['GET'])
def get_areas():
    """Get list of available areas"""
    return jsonify({'areas': unique_areas})

@app.route('/api/crops', methods=['GET'])
def get_crops():
    """Get list of available crops"""
    return jsonify({'crops': unique_items})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get basic statistics about the model"""
    return jsonify({
        'total_areas': len(unique_areas),
        'total_crops': len(unique_items),
        'model_loaded': model is not None,
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

def generate_insights(area, item, year, rainfall, pesticides, temperature, prediction):
    """Generate insights based on the prediction"""
    insights = []
    
    # Rainfall insights
    if rainfall < 500:
        insights.append("⚠️ Low rainfall detected. Consider irrigation systems for optimal yield.")
    elif rainfall > 2000:
        insights.append("🌧️ High rainfall detected. Ensure proper drainage to prevent waterlogging.")
    else:
        insights.append("✅ Rainfall levels are optimal for crop growth.")
    
    # Temperature insights
    if temperature < 10:
        insights.append("❄️ Low temperature may slow crop growth. Consider greenhouse farming.")
    elif temperature > 35:
        insights.append("🔥 High temperature detected. Ensure adequate irrigation and shade.")
    else:
        insights.append("🌡️ Temperature is within optimal range for crop cultivation.")
    
    # Pesticides insights
    if pesticides < 50:
        insights.append("🌱 Low pesticide usage. Monitor for pest infestations.")
    elif pesticides > 1000:
        insights.append("⚠️ High pesticide usage. Consider integrated pest management.")
    else:
        insights.append("🛡️ Pesticide levels are balanced for crop protection.")
    
    # Yield prediction insights
    if prediction > 100000:
        insights.append("🎉 Excellent yield potential! Maintain current practices.")
    elif prediction > 50000:
        insights.append("👍 Good yield expected. Minor optimizations could improve results.")
    else:
        insights.append("📈 Yield can be improved. Consider soil testing and nutrient management.")
    
    return insights

if __name__ == '__main__':
    if model is None:
        print("❌ Model not loaded. Please run model_training.py first.")
    else:
        print("🚀 Starting Crop Yield Prediction API...")
        app.run(debug=True, host='0.0.0.0', port=5000) 