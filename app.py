#!/usr/bin/env python
# coding: utf-8

# In[10]:


from nicegui import ui
import pickle as p


# In[11]:


with open(r'news-model.pkl', 'rb') as f:
    model = p.load(f)

with open(r'vectorizer.pkl', 'rb') as f:
    vectorizer = p.load(f)


# In[16]:


def classify(text):
    if not text.strip():
        return "Please enter some text."
    
    # Transform the input text
    X = vectorizer.transform([text])
    
    # Predict the class (this will be a single integer, e.g., 0, 1, 2, or 3)
    pred = model.predict(X)[0]
    
    # Map numeric label to category
    label_map = {
        0: 'World',
        1: 'Sports',
        2: 'Business',
        3: 'Tech/Sci-fi'
    }
    
    category = label_map.get(pred, "Unknown")
    
    return f"Predicted category: {category}"

with ui.column().classes('w-full max-w-2xl mx-auto p-6 space-y-4 bg-white shadow-lg rounded-xl'):
    ui.label("📰 News Classifier") \
        .classes("text-3xl font-bold text-center text-blue-700")

    input_text = ui.textarea(
        label="Paste your news article here...",
        placeholder="Type or paste news text..."
    ).classes("w-full h-40 border-blue-300 focus:border-blue-500")

    result_label = ui.label("Result will appear here.") \
        .classes("text-lg text-gray-700 font-medium text-center")

    def on_classify():
        result_label.text = classify(input_text.value)

    ui.button("🔍 Classify", on_click=on_classify) \
        .classes("bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2 rounded-lg")

ui.run()





