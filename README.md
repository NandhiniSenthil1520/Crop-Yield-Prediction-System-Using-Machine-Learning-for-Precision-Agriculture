# 🌾 Crop Yield Prediction System

**Developed by Nandhini S**  
**Department of Artificial Intelligence and Data Science**  
**Dr. N. G. P. Institute of Technology**

## 📋 Project Overview

This is an AI-powered web application that predicts crop yields using machine learning algorithms. The system analyzes various environmental factors including temperature, rainfall, pesticide usage, and geographical data to provide accurate yield predictions and actionable insights for farmers and agricultural planners.

## ✨ Features

- **🤖 AI-Powered Predictions**: Decision Tree Regressor model trained on extensive agricultural datasets
- **🌍 Global Coverage**: Support for multiple countries and crop types worldwide
- **💡 Smart Insights**: Actionable recommendations to optimize farming practices
- **📊 Real-time Analysis**: Instant predictions with confidence scores
- **🎨 Modern UI**: Beautiful, responsive design with intuitive user interface
- **📱 Mobile Friendly**: Works seamlessly on desktop, tablet, and mobile devices

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**
- **Flask**: Web framework for API development
- **scikit-learn**: Machine learning library for model training
- **pandas & numpy**: Data processing and numerical computations
- **joblib**: Model serialization and loading

### Frontend
- **HTML5 & CSS3**: Modern web standards
- **Tailwind CSS**: Utility-first CSS framework
- **JavaScript (ES6+)**: Dynamic functionality
- **Font Awesome**: Beautiful icons

### Machine Learning
- **Decision Tree Regressor**: Core prediction algorithm
- **Label Encoding**: Categorical variable preprocessing
- **Feature Engineering**: Optimized input processing

## 📁 Project Structure

```
crop yield/
├── data/                          # Dataset files
│   ├── yield_df.csv              # Main yield dataset
│   ├── temp.csv                  # Temperature data
│   ├── rainfall.csv              # Rainfall data
│   └── pesticides.csv            # Pesticide usage data
├── models/                       # Trained models and encoders
│   ├── crop_yield_model.pkl      # Trained ML model
│   ├── area_encoder.pkl          # Country/area encoder
│   ├── item_encoder.pkl          # Crop type encoder
│   ├── unique_areas.txt          # Available countries
│   └── unique_items.txt          # Available crops
├── templates/                    # HTML templates
│   └── index.html               # Main application page
├── app.py                       # Flask backend API
├── model_training.py            # Model training script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd crop-yield-prediction
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Train the Model
```bash
python model_training.py
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## 📊 Dataset Information

The application uses comprehensive agricultural datasets including:

- **Yield Data**: Historical crop yield data from various countries
- **Weather Data**: Temperature and rainfall patterns
- **Agricultural Practices**: Pesticide usage and farming methods
- **Geographical Data**: Country-specific agricultural information

### Data Sources
- Global agricultural databases
- Weather monitoring systems
- Agricultural census data
- Environmental monitoring networks

## 🧠 Machine Learning Model

### Model Architecture
- **Algorithm**: Decision Tree Regressor
- **Features**: 6 input parameters
- **Output**: Crop yield prediction (hg/ha)
- **Performance**: Optimized for accuracy and interpretability

### Input Parameters
1. **Country/Area**: Geographical location
2. **Crop Type**: Type of crop being cultivated
3. **Year**: Growing season year
4. **Rainfall**: Average annual rainfall (mm)
5. **Pesticides**: Pesticide usage (tonnes)
6. **Temperature**: Average temperature (°C)

### Model Performance
- **R² Score**: Measures prediction accuracy
- **Mean Squared Error**: Error metric
- **Confidence Score**: Prediction reliability indicator

## 🎯 Usage Guide

### Making Predictions
1. **Select Country**: Choose your country from the dropdown
2. **Choose Crop**: Select the crop type you want to predict
3. **Enter Year**: Specify the growing season year
4. **Input Weather Data**: Provide rainfall and temperature values
5. **Add Agricultural Data**: Enter pesticide usage information
6. **Get Prediction**: Click "Predict Yield" for instant results

### Understanding Results
- **Yield Prediction**: Expected crop yield in hg/ha
- **Confidence Score**: Model's confidence in the prediction
- **AI Insights**: Actionable recommendations for optimization
- **Input Summary**: Review of your entered parameters

## 🔧 API Endpoints

### Prediction Endpoint
```
POST /api/predict
```
**Request Body:**
```json
{
    "area": "india",
    "item": "wheat",
    "year": 2024,
    "rainfall": 1000,
    "pesticides": 100,
    "temperature": 25
}
```

### Data Endpoints
- `GET /api/areas` - Get available countries
- `GET /api/crops` - Get available crop types
- `GET /api/stats` - Get model statistics

## 🎨 UI/UX Features

### Design Principles
- **Clean & Modern**: Minimalist design with focus on usability
- **Responsive**: Adapts to all screen sizes
- **Accessible**: Easy to use for farmers of all technical levels
- **Intuitive**: Clear navigation and user flow

### Color Scheme
- **Primary**: Green tones (agricultural theme)
- **Secondary**: Blue and purple gradients
- **Accent**: Orange and yellow for highlights

## 🔮 Future Enhancements

### Planned Features
- **IoT Integration**: Real-time sensor data input
- **Weather API**: Automatic weather data retrieval
- **Mobile App**: Native mobile application
- **Advanced Analytics**: Detailed trend analysis
- **Multi-language Support**: Regional language support

### Model Improvements
- **Deep Learning**: Neural network implementations
- **Ensemble Methods**: Multiple model combinations
- **Real-time Learning**: Continuous model updates
- **Disease Detection**: Plant health monitoring

## 🤝 Contributing

We welcome contributions to improve the crop yield prediction system. Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is developed for educational and research purposes at Dr. N. G. P. Institute of Technology.

## 👨‍💻 Developer

**Nandhini S**  
Department of Artificial Intelligence and Data Science  
Dr. N. G. P. Institute of Technology

## 📞 Support

For technical support or questions about the project, please contact:
- Email: [nandhinisenthil1920@gmail.com]

---

**🌱 Empowering Agriculture with Artificial Intelligence**  
*Making farming smarter, more efficient, and more sustainable through the power of machine learning.* 