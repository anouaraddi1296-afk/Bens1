import os
import requests
import json

API_KEY = os.environ.get("OPENROUTER_API_KEY")

# يمكنك تغيير اسم النموذج هنا إذا أردت
MODEL_NAME = "openrouter/free" 

print("Sending request to OpenRouter...")

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": "Explain the concept of ICT Fair Value Gap in one sentence."}
        ]
    })
)

if response.status_code == 200:
    ai_reply = response.json()['choices'][0]['message']['content']
    print(f"\n--- AI Response ---\n{ai_reply}")
else:
    print(f"Error: {response.status_code} - {response.text}")
