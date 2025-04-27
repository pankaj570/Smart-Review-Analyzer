import os
import google.generativeai as genai

genai.configure(api_key='AIzaSyD0TfyvUF4VNpYCukKw49K4CSNH_ftUVxc')

def generate_response(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
    response = model.generate_content(prompt)
    return response.text
