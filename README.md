Project Description- VitaScan AI Agent - Steve is a desktop-based health diagnostic tool that leverages Artificial Intelligence to identify potential vitamin deficiencies. Built using Python’s Tkinter for the interface and HuggingFace’s Transformer models, the application utilizes "Zero-Shot Classification." Unlike traditional search engines that require specific keywords, Steve can interpret natural language descriptions—such as "I feel tired and my eyes hurt"—and map them to the most likely nutrient deficiency. Once identified, the agent provides a comprehensive breakdown of the vitamin’s scientific name, biological functions, and dietary sources (both plant and animal) to help the user recover.

Objectives:-The primary objective of VitaScan is to bridge the gap between vague physical symptoms and actionable nutritional data. By providing an immediate "AI Analysis," the tool aims to:
(i)Educate users on the specific roles vitamins play in bodily functions (e.g., Vitamin K’s role in blood clotting).
(ii)Demystify scientific terminology like "Retinol" or "Phylloquinone" for the average person.
(iii)Promote Dietary Wellness by suggesting natural food sources as a first line of defense against minor health issues.
(iv)Reduce Cognitive Load by using AI to handle the "search and filter" process, giving the user a single, clean result instead of thousands of confusing web links.

Target Audience:- VitaScan is designed for a broad spectrum of health-conscious individuals who prefer a tech-driven approach to wellness. This includes students and researchers looking for a quick reference for micronutrients, fitness enthusiasts seeking to optimize their diet based on how they feel, and elderly users who may find navigating complex medical websites difficult. Additionally, it serves as an excellent tool for educators to demonstrate the practical application of Natural Language Processing (NLP) in healthcare. It is particularly useful for anyone experiencing minor, non-emergency symptoms who wants to check their nutritional intake before consulting a professional.

Scope of this project:- The current scope of the application is focused on the six primary vitamin groups (A, B, C, D, E, and K) and their most common deficiency markers. Technically, the app operates as a local GUI application using the BART-large-mnli model for high-accuracy text classification. While it offers detailed dietary remedies, the scope is strictly informational and educational; it is not intended to replace professional medical diagnosis or clinical bloodwork. Future iterations could expand the scope to include mineral deficiencies (like Iron or Magnesium), integration with wearable health data, and the ability to export "Health Reports" in PDF format for doctor consultations.

Setup Instructions
Follow these steps to get Steve running on your computer:
1. Install Python
Ensure you have Python installed (Version 3.8 or higher is recommended). You can download it from python.org.

2. Install Required Libraries
Steve relies on two main components: Tkinter (for the window) and Hugging Face Transformers (for the AI). Open your terminal or command prompt and run:

Install the following on your computer:

pip install torch torchvision torchaudio
pip install transformers

Note: The first time you run the app, it will download the facebook/bart-large-mnli model (about 1.6GB). You only need to do this once!

3. Save the Script
Copy the code provided in the VitaScan AI Agent- Steve App.py file.

Save it on your computer as vitascan.py.

How to Use Steve:

Launch the App:

Run the script by typing python vitascan.py in your terminal or double-clicking the file.

Describe Your Symptoms:
In the text box labeled "Describe how you feel?", type your symptoms in plain English.

Example: "My eyes feel very dry and I can't see well at night" or "I feel very tired and my muscles are weak."

Get Analysis:
Click the red "Get AI Analysis" button.

Review Results:
Steve will process your text using a Neural Network and display:

The Suggested Vitamin (e.g., Vitamin A).

Scientific Name (e.g., Retinol).

Key Functions of that vitamin.

Food Sources to help you recover.
