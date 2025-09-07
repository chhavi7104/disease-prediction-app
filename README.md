# Disease-prediction-app
<h2> Epics Project  </h2>
# 🧠  Disease Prediction Website using Machine Learning

Welcome to the **Visual AI**, a web-based platform that uses cutting-edge **Machine Learning** and **Retinopathy** analysis to predict the risk of **Diabetes**, **Hypertension**, and **Autism**. This project aims to support early diagnosis and assist healthcare professionals with advanced, accessible, and interpretable tools.

---

## 🚀 Features 
 
- 🔍 **Disease Prediction**: Predicts risk levels for:
  - **Diabetes**
  - **Hypertension**
  - **Autism Spectrum Disorder (ASD)**
  
- 🧠 **Machine Learning Models**: Trained using clinical and visual data to deliver high-accuracy predictions.

- 👁️ **Retinopathy-Based Analysis**: For Diabetes and Hypertension, retina image analysis enhances prediction using deep learning.

- 📈 **User-Friendly Interface**: Intuitive web interface for uploading data, viewing results, and understanding risk.

- 🔒 **Secure & Private**: All patient data is kept confidential and processed locally (or securely).

---

## 🧪 Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Backend**: Python (Flask / Django)
- **Machine Learning**: Scikit-learn, TensorFlow, OpenCV
- **Image Processing**: Retina scans via CNN models
- **Autism Prediction**: Survey/questionnaire-based input + ML classifier
- **Database**: SQLite / PostgreSQL (Optional)

---

## 📊 Dataset Sources

- **Diabetes**: Pima Indians Diabetes Dataset
- **Hypertension**: Public health records and retinal scan datasets
- **Autism**: Autism Screening Adult/Child datasets from UCI Machine Learning Repository
- **Retinopathy**: Kaggle Diabetic Retinopathy Detection Dataset

---

## 🛠️ Installation Guide

```bash
# Clone the repository
git clone https://github.com/your-username/disease-prediction-site.git
cd disease-prediction-site

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
