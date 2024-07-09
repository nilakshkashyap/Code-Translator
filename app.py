# Before running the code run `pip install -r requirements.txt` in the terminal

import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv
import os

# Load the .env file
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

    st.markdown("""
    <h2>Project Description</h2>
    <p>CodeXchange is an innovative web application designed to streamline code translation and facilitate seamless collaboration among developers working with different programming languages. Whether you're transitioning applications between platforms, collaborating in multilingual teams, or reusing code across projects, CodeXchange empowers developers to effortlessly translate code snippets between various programming languages. Leveraging advanced translation algorithms and syntax analysis, CodeXchange ensures accurate and reliable code conversion while preserving the original functionality and logic. With its intuitive interface and comprehensive language support, CodeXchange revolutionizes the development workflow, enabling teams to work together efficiently, enhance code reusability, and accelerate project delivery.</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2>Scenario 1: Platform Transition</h2>
    <p>CodeXchange assists developers in transitioning applications from one platform to another. For instance, a team working on an application written in Python needs to migrate it to Java to leverage Java's robustness and scalability in an enterprise environment. By inputting the Python code snippets and selecting Java as the target language, developers receive accurately translated code that maintains the original functionality, streamlining the migration process and minimizing the risk of introducing errors.</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2>Scenario 2: Multilingual Collaboration</h2>
    <p>In a collaborative project where team members use different programming languages, CodeXchange facilitates seamless integration by translating code snippets as needed. Suppose one part of the team is proficient in C++ while another prefers Python. Developers can write code in their preferred language and use CodeXchange to translate it, ensuring all team members can work together efficiently without being constrained by language barriers. This enhances productivity and reduces the learning curve associated with adopting new languages.</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2>Scenario 3: Code Reusability Across Projects</h2>
    <p>CodeXchange promotes code reusability by enabling developers to translate existing code into different languages for new projects. For example, a developer has written a set of utility functions in Java that would be beneficial for a new project being developed in C++. By translating these Java functions into C++ using CodeXchange, the developer can quickly integrate proven code into the new project, saving time and ensuring consistency across different projects.</p>
    """, unsafe_allow_html=True)

    st.subheader("Code Translation")
    source_code_snippet = st.text_area("Enter the code snippet you want to translate:")
    target_language = st.selectbox("Select the target programming language:", ["Python", "Java", "C++"])
    if st.button("Translation Code"):
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
    