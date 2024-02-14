 
import streamlit as st
import requests
from pathlib import Path
import google.generativeai as genai

genai.configure(api_key="AIzaSyAtvEb6PVk_rGe0j6egUlWlRH_nX1I4u1Q")

generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

response = requests.get("https://fleastore.in/gem/img.png")
response.raise_for_status()

with open("img.png", "wb") as f:
    f.write(response.content)

if not (img := Path("img.png")).exists():
  raise FileNotFoundError(f"Could not find image: {img}")

image_parts = [
  {
    "mime_type": "image/png",
    "data": Path("img.png").read_bytes()
  },
]

predefined_prompt = "Read image and Detect Dark patterns in the image and if you find no dark pattern then just say there is no dark pattern"
prompt_parts = [
  {
    "text": predefined_prompt,
  },
  image_parts[0],
]

response = model.generate_content(prompt_parts)


st.write(response.text)
