# Before running the code run `pip install -r requirements.txt` in the terminal

import streamlit as st
import google.generativeai as palm

palm.configure(api_key="AIzaSyCzo6ZghwFxUz_aZi5WcKJvpklqXv9vl74")

#Define the model to use
model_name="models/chat-bison-001"

#Function to translate code from one language to another
def translate_code(code_snippet, target_language):
    prompt=f"Translate the following code to {target_language}:\n\n{code_snippet}"
    response=palm.chat(
        model=model_name,
        messages=[prompt]
    )
    return response.candidates[0]["content"]
