import requests

HUGGINGFACE_TOKEN = "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"
headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

# Step 1: Emotion Detection using a pretrained model
def analyze_emotion(user_input):
    url = "https://api-inference.huggingface.co/models/bhadresh-savani/distilbert-base-uncased-emotion"
    payload = {"inputs": user_input}
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    
    if isinstance(result, list):
        emotions = result[0]
        top_emotion = max(emotions, key=lambda x: x['score'])
        return f"Detected emotion: {top_emotion['label'].capitalize()} ({top_emotion['score']:.2f})"
    else:
        return "Emotion detection failed. Try again."

# Step 2: Generate reflection based on detected emotion
def reframe_emotion(user_input, style="Stoic"):
    prompt = (
        f"You are a {style} philosopher. A user feels:\n"
        f"{user_input}\n\n"
        f"Write a short and compassionate reflection using a {style} mindset."
    )
    url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 150}}
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    
    try:
        return result[0]["generated_text"]
    except:
        return "Reframing failed. Try again."
