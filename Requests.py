import base64
import requests
from dotenv import dotenv_values

#get the api key from the .env file
config = dotenv_values(".env")

# OpenAI API Key
api_key = config["OPENAI_API_KEY"]

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "images/6_apples.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Return a JSON object with the number of apples in the image. For example, if the image has 12 apples, 24 oranges and 5 bananas, the JSON object should be {\"apples\": 12, \"oranges\":24, \"bananas\": 5}. It is very important you return NOTHING except for the JSON object as the output will be used in code."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())