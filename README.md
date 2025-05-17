PlugBot 💬
PlugBot is a lightweight, customizable Flask-based chatbot backend designed to be easily plugged into any frontend application. It provides a flexible foundation for intelligent chat interactions in web apps, educational platforms, or custom deployments.

🔧 Features
🧠 Intent-based chatbot logic using a JSON structure

⚡ Fast Flask API for seamless frontend integration

🧩 Easily pluggable into any frontend framework (React, Vanilla JS, Vue, etc.)

🔁 Supports both short, intent-driven queries and long-form conversational fallback

🤖 Integrates Hugging Face DialoGPT-medium as a fallback for handling unexpected queries

🛠️ Fully customizable intents and responses


## 🚀 Running Locally

1. Clone the repo :

```bash
git clone https://github.com/mhtbtanvir/PlugBot.git
cd PlugBot/chatbot-deployment
python -m venv venv
venv/Scripts/activate
pip install Flask torch torchvision nltk
```
Modify the json file with different intents and responses for your Chatbot

To Train :
```bash
python train.py
```
To Run the Model :
```bash
python app.py
```
The chatbot will first attempt to answer queries based on your trained intent classification model. If it cannot confidently match an intent, it will fallback to Hugging Face’s DialoGPT-medium for a more conversational response.
Chat on Bash:
 .```bash
python chat.py```
*Credits:*
This repo is a modified version from https://github.com/patrickloeber/chatbot-deployment/
