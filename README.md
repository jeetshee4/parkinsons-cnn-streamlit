# 🧠 Parkinson’s Disease Prediction using CNN (Handwriting Data)
**🔍 Project Overview**

This project aims to predict Parkinson’s Disease based on hand-drawn images (spiral and wave patterns).
Using a Convolutional Neural Network (CNN) model, the system analyzes handwriting patterns and distinguishes between healthy and Parkinson’s-affected individuals.

The model is deployed as an interactive Streamlit web app, allowing users to upload their handwriting images and get real-time predictions.

**🚀 Live Demo**

👉 Try the App on Streamlit Cloud
 (replace with your actual link after deployment)

**🧩 Features**

1. 🧬 Predicts Parkinson’s Disease from spiral or wave handwriting drawings

2. 📷 Accepts image uploads directly in the browser

3. ⚡ Built with Convolutional Neural Networks (CNN) for feature extraction

4. 🧠 Real-time inference using a pre-trained .h5 model

5. 🎨 Clean and responsive Streamlit interface

6. 📊 Visualizes training accuracy and loss




| Component            | Technology Used                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------- |
| Frontend             | Streamlit                                                                                            |
| Backend              | TensorFlow / Keras                                                                                   |
| Programming Language | Python                                                                                               |
| Image Processing     | Pillow (PIL)                                                                                         |
| Dataset              | [KMader / Parkinson’s Drawings (Kaggle)](https://www.kaggle.com/datasets/kmader/parkinsons-drawings) |



**📁 Project Structure**

```
📦 Parkinsons_CNN_App/
│
├── app.py                # Streamlit web app
├── parkinson_model.h5              # Trained CNN model
├── class_indices.json    # Class label mappings
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── /drawings             # Dataset (spiral, wave images)
```


**⚙️ Installation & Setup**


1️⃣ Clone the repository
```
git clone https://github.com/jeetshee4/parkinsons-cnn-streamlit.git
cd parkinsons-cnn-streamlit
```

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run locally
streamlit run app.py

 

***🧮 Model Overview***

The CNN model was trained using the Parkinson’s Drawings dataset, containing spiral and wave drawings labeled as healthy or parkinson.
The architecture includes:

3 Convolutional layers with Batch Normalization and MaxPooling

Dense layer for feature interpretation

Dropout for regularization

Softmax output for binary classification

📈 Training Summary
Metric	Value
Image Size	224×224
Batch Size	32
Epochs	20
Optimizer	Adam
Loss Function	Categorical Crossentropy
💬 Example Prediction

Upload a spiral or wave drawing → model predicts:

🧠 Predicted Class: Parkinson’s


or

✅ Predicted Class: Healthy


**🧑‍💻 Author**

Jeet Shee
📧 biswanathshee87@gmail.com

💻 GitHub: jeetshee4


**🏁 Future Enhancements**

🔁 Train on larger handwriting datasets for improved accuracy

📊 Add Grad-CAM visualization to show feature attention

☁️ Integrate a backend API for multi-model deployment