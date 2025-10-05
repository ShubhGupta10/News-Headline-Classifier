📰 News Headline Classifier

A simple NLP-powered web app that classifies news headlines into categories like Business, Sci-Fi/Tech, Sports, or World.
Built as a personal project to explore text classification and experiment with machine learning on real-world text data.

🚀 Features

Classifies any news headline into one of four categories.

Interactive dashboard built with NiceGUI.

Uses TF-IDF Vectorization and a Multinomial Naive Bayes model from scikit-learn.

Lightweight, fast, and easy to extend with new categories.

🧠 Tech Stack

Language: Python

Libraries: scikit-learn, pandas, re, pickle, nicegui

Core ML Tools: TfidfVectorizer, MultinomialNB

⚙️ Installation

Clone the repository:

git clone https://github.com/ShubhGupta10/news-headline-classifier.git
cd news-headline-classifier


Install dependencies:

pip install -r requirements.txt


Run the app:

python app.py


Open your browser and go to:

http://localhost:8080

💡 How It Works

The model reads the input headline.

Text is cleaned and vectorized using TF-IDF.

The trained MultinomialNB classifier predicts the news category.

The dashboard instantly displays the result.

A pre-trained model file (model.pkl) is already included — no retraining required.

🗂️ Project Structure
news-headline-classifier/
│
├── app.py                # Main NiceGUI dashboard
├── model.pkl             # Trained classifier
├── vectorizer.pkl        # TF-IDF vectorizer
├── requirements.txt      # Dependencies
├── /data                 # Dataset used for training
└── README.md

🖼️ Demo

<img width="935" height="540" alt="image" src="https://github.com/user-attachments/assets/8b7ece8b-6a0d-4db0-9c51-8741f9183b96" />


👨‍💻 Author

Created by Shubh Gupta
GitHub: [Shubh Gupta](https://github.com/ShubhGupta10)
