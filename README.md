# PlugBot 💬

**PlugBot** is a lightweight, customizable Flask-based chatbot backend designed to be plugged into any frontend application. It serves as a flexible foundation for intelligent chat interactions in web apps, educational platforms, or custom deployments.

---

## 🔧 Features

- 🧠 Intent-based chatbot logic using a JSON structure
- ⚡ Fast Flask API for integration
- 🧩 Easily pluggable into any frontend (e.g. React, Vanilla JS, Vue)
- 🔁 Supports both short and long-form questions
- 🛠️ Fully customizable intents and responses
- 🧪 Designed for educational, EdTech, or utility bots



---

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
Chat on Bash:
 .```bash
python chat.py```
*Credits:*
This repo is a modified version from https://github.com/patrickloeber/chatbot-deployment/
