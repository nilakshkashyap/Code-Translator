# Before running the code run `pip install -r requirements.txt` in the terminal

import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv
import os

#Load the .env file
load_dotenv()

# Access the API key
gemini_api_key = os.getenv('GEMINI_API_KEY')

# Configure the API key
palm.configure(api_key=gemini_api_key)

# Define the model to use
model_name = "models/chat-bison-001"


# Function to translate code from one language to another
def translate_code(code_snippet, target_language):
    prompt = f"Translate the following code to {target_language}:\n\n{code_snippet}"
    response = palm.chat(
        model=model_name,
        messages=[prompt]
    )
    return response.candidates[0]["content"]


# Streamlit application
def main():

    st.title("CodeXchange: Ai-Powered Code Translation Tool")
   
    st.markdown(
        """
        <style>

        # .stTextArea{
        #     margin: 16px
        # }

        .main .block-container {
        max-width: 1000px;
        padding: 1rem;
    }

    .stSelectbox{
        max-width: 25%
    }

        .use-case-container{
    min-height: 30vh;
    display: flex;
    justify-content: space-evenly;
    font-family: "Source Sans Pro", sans-serif;
}

.use-case-item{
    flex-grow: 1;
    margin: 48px auto;
    margin-right: 16px;
    padding: 16px;
    color: rgba(245, 245, 245, 0.925);
    border: 2px solid rgb(59, 165, 165);
}

.use-case-title{
    font-weight: 800;
    font-size: 24px;
}
.use-case-description{
    font-weight: 400;
    font-size: 16px;
    line-height: 2rem;
    color: #9e9d9d;
}
        """, unsafe_allow_html=True
    )

    st.markdown(
        f"""
       <div class="use-case-container">
        <div class="use-case-item">
            <div class="use-case-title">
                <p>Platform Transition</p>
            </div>
            <div class="use-case-description">
                <p>Easily migrate your codebase from one programming language to another, ensuring seamless platform transition and reducing development time.</p>
            </div>
        </div>
        <div class="use-case-item">
            <div class="use-case-title">
                <p>Multilingual Collaboration</p>
            </div>
            <div class="use-case-description">
                <p>Facilitate collaboration among developers who prefer different programming languages by translating code, enabling a more inclusive and productive team environment</p>
            </div>
        </div>
        <div class="use-case-item">
            <div class="use-case-title">
                <p>Code Reusability</p>
            </div>
            <div class="use-case-description">
                <p>Maximize code reuse by translating existing code into different languages for various projects, ensuring consistency and saving time on development.</p>
            </div>
        </div>
    </div>
        """, unsafe_allow_html=True
    )

    

    source_code_snippet = st.text_area("Enter the code snippet you want to translate:")
    target_language = st.selectbox("Select the target programming language:", ["Python", "Java", "C++"])
    if st.button("Translate"):
        if source_code_snippet.strip():
            with st.spinner("Translating code..."):
                try:
                    translated_code = translate_code(source_code_snippet, target_language)
                    st.success("Code translation complete!")
                    st.code(translated_code, language=target_language.lower())
                except Exception as e:
                    st.error(f"Error translating code: {e}")
        else:
            st.error("Please enter a code snippet.")


if __name__ == "__main__":
    main()
    