# %%
from openai import OpenAI
import base64
import requests
from dotenv import dotenv_values

client = OpenAI()

#get the api key from the .env file
config = dotenv_values(".env")

# OpenAI API Key
api_key = config["OPENAI_API_KEY"]

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def read_image(prompt, image_path):
    # Function to encode the image

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
            "text": "Return a dictionary based on the content in the image which contains: {\"type of food\": \"number of items\"}"
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

    return response.json()["choices"][0]["message"]["content"]


def request(prompt, system_message="you are a helpful assistant", model="gpt-3.5-turbo-16k", temperature=0.8):

    summary = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )

    return summary.choices[0].message.content


class Chat():
    def __init__(self, system_message, ignore_base_system_message=False):
        if not ignore_base_system_message:
            system_message = f"""{system_message}"""
        
        self.messages = [
            {"role": "system", "content": system_message},
        ]
        # self.summary = None

    def add_assistant_msg(self, msg):
        self.messages.append({"role": "assistant", "content": msg})

    def __call__(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=self.messages
        )
        return response.choices[0].message.content
# %%
