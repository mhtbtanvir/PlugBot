import random
import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Load intent model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Load Hugging Face fallback model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
hf_model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

chat_history_ids = None  # maintain conversation context

bot_name = "TM"


hf_turn_count = 0  # global variable to track turns


def get_hf_response(user_input):
    global chat_history_ids, hf_turn_count
    new_input_ids = tokenizer.encode(
        user_input + tokenizer.eos_token, return_tensors='pt')

    # Append to chat history if it exists
    bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) \
        if chat_history_ids is not None else new_input_ids

    # Create attention mask
    attention_mask = torch.ones(bot_input_ids.shape, dtype=torch.long)

    # Generate with sampling to avoid repetition
    chat_history_ids = hf_model.generate(
        bot_input_ids,
        attention_mask=attention_mask,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
    )

    hf_turn_count += 1
    if hf_turn_count >= 6:
        chat_history_ids = None  # reset conversation context
        hf_turn_count = 0

    # Decode only the new generated tokens
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )
    return response


def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])

    # Use Hugging Face as fallback
    return get_hf_response(msg)


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        sentence = input("You: ")
        if sentence.lower() == "quit":
            break

        resp = get_response(sentence)
        print(f"{bot_name}: {resp}")
