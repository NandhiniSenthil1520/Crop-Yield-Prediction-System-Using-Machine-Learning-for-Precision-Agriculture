import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import warnings
warnings.filterwarnings('ignore')

def load_and_preprocess_data():
    """Load and preprocess the crop yield datasets"""
    print("Loading datasets...")
    
    # Load the main yield dataset
    yield_df = pd.read_csv('data/yield_df.csv')
    
    # Load additional datasets for feature engineering
    temp_df = pd.read_csv('data/temp.csv')
    rainfall_df = pd.read_csv('data/rainfall.csv')
    pesticides_df = pd.read_csv('data/pesticides.csv')
    
    print(f"Main dataset shape: {yield_df.shape}")
    print(f"Temperature dataset shape: {temp_df.shape}")
    print(f"Rainfall dataset shape: {rainfall_df.shape}")
    print(f"Pesticides dataset shape: {pesticides_df.shape}")
    
    # Clean the main dataset
    yield_df = yield_df.dropna()
    
    # Convert Area and Item to lowercase for consistency
    yield_df['Area'] = yield_df['Area'].str.lower()
    yield_df['Item'] = yield_df['Item'].str.lower()
    
    # Create feature encoders
    area_encoder = LabelEncoder()
    item_encoder = LabelEncoder()
    
    # Encode categorical variables
    yield_df['area_encoded'] = area_encoder.fit_transform(yield_df['Area'])
    yield_df['item_encoded'] = item_encoder.fit_transform(yield_df['Item'])
    
    # Select features for the model
    features = ['area_encoded', 'item_encoded', 'Year', 'average_rain_fall_mm_per_year', 
                'pesticides_tonnes', 'avg_temp']
    target = 'hg/ha_yield'
    
    X = yield_df[features]
    y = yield_df[target]
    
    # Save encoders for later use
    joblib.dump(area_encoder, 'models/area_encoder.pkl')
    joblib.dump(item_encoder, 'models/item_encoder.pkl')
    
    # Save unique areas and items for the frontend
    unique_areas = sorted(yield_df['Area'].unique())
    unique_items = sorted(yield_df['Item'].unique())
    
    with open('models/unique_areas.txt', 'w') as f:
        for area in unique_areas:
            f.write(f"{area}\n")
    
    with open('models/unique_items.txt', 'w') as f:
        for item in unique_items:
            f.write(f"{item}\n")
    
    return X, y, unique_areas, unique_items

def train_model(X, y):
    """Train the Decision Tree Regressor model"""
    print("Training Decision Tree Regressor...")
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = DecisionTreeRegressor(random_state=42, max_depth=10)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Performance:")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.4f}")
    
    # Save the model
    joblib.dump(model, 'models/crop_yield_model.pkl')
    
    return model, X_test, y_test, y_pred

def main():
    """Main function to train the model"""
    print("🌾 Crop Yield Prediction Model Training")
    print("=" * 50)
    
    # Create models directory if it doesn't exist
    import os
    os.makedirs('models', exist_ok=True)
    
    # Load and preprocess data
    X, y, unique_areas, unique_items = load_and_preprocess_data()
    
    # Train the model
    model, X_test, y_test, y_pred = train_model(X, y)
    
    print("\n✅ Model training completed successfully!")
    print(f"📊 Available crop types: {len(unique_items)}")
    print(f"🌍 Available countries: {len(unique_areas)}")
    print("\nModel saved to: models/crop_yield_model.pkl")
    print("Encoders saved to: models/area_encoder.pkl, models/item_encoder.pkl")

if __name__ == "__main__":
    main() 