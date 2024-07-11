# Before running the code run `pip install -r requirements.txt` in the terminal

import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv
import os,re,sys

#Load the .env file
load_dotenv()

# Access the API key
gemini_api_key = os.getenv('GEMINI_API_KEY')

# Configure the API key
palm.configure(api_key=gemini_api_key)

# Define the model to use
model_name = "models/chat-bison-001"
languages = ["Python", "Java", "C++"]


# Function to translate code from one language to another
def translate_code(code_snippet, target_language):
    instruction = "Give Fully runnable code. Include syntax highlighting. Give only the translated code"
    prompt = f"Translate the following code to {target_language}:\n\n{code_snippet}"
    try:
        response = palm.chat(
            model=model_name,
            messages=[instruction,prompt]
        )
    except google.api_core.exceptions.DeadlineExceeded:
        print("Timeout. Please Try again")
        exit()
    return response.candidates[0]["content"]


def extractCode(code):
    try:
        markdown_pattern = re.compile(r"(```[.<>\[\]\{\}#\w\s\\n\(\);,+=\":/]*```)\s*(?:.*)$")
        markdown_code = re.search(markdown_pattern,code).group(1)
        markdown_pattern = re.compile(r"`.*")
        markdown_code = str(re.sub(markdown_pattern,"",markdown_code))
        return markdown_code
    except IndexError:
        print("Timeout. Please Try again")
        exit()



def commandLine(targetLanguage):
    inputFileName = outputFileName = ""
    if len(sys.argv) < 4:
        outputFileName = "converted.txt"
    else:
        outputFileName = sys.argv[3]
    inputFileName = sys.argv[2]
    code = ""
    with open(inputFileName,"r") as inputFile:
        code = inputFile.read()

    with open(outputFileName,"w") as outputFile:
        print("\rConverting...")
        translated_code = extractCode(translate_code(code,targetLanguage))
        print("\rConverted...")
        print("\rSaving...")
        outputFile.write(translated_code)
        print("\rOutput Saved...\n\n")
        print(f"{targetLanguage.title()} Code:")
        print(translated_code)

# Streamlit application
def main():

    st.title("CodeXchange: Ai-Powered Code Translation Tool")
    st.write("""
             <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
             """,unsafe_allow_html=True)
    st.markdown(
        """
        <style>


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
    box-shadow: 5px 5px rgba(0, 255, 255, 0.658);
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
                <span class="material-symbols-outlined"> compare_arrows</span>
            </div>
            <div class="use-case-description">
                <p>Easily migrate your codebase from one programming language to another, ensuring seamless platform transition and reducing development time.</p>
            </div>
        </div>
        <div class="use-case-item">
            <div class="use-case-title">
                <p>Multilingual Collaboration</p>
                <span class="material-symbols-outlined">groups</span>
            </div>
            <div class="use-case-description">
                <p>Facilitate collaboration among developers who prefer different programming languages by translating code, enabling a more inclusive and productive team environment</p>
            </div>
        </div>
        <div class="use-case-item">
            <div class="use-case-title">
                <p>Code Reusability</p>
                <span class="material-symbols-outlined">cycle</span>
            </div>
            <div class="use-case-description">
                <p>Maximize code reuse by translating existing code into different languages for various projects, ensuring consistency and saving time on development.</p>
            </div>
        </div>
    </div>
        """, unsafe_allow_html=True
    )

    

    source_code_snippet = st.text_area("Enter the code snippet you want to translate:")
    target_language = st.selectbox("Select the target programming language:",languages)
    if st.button("Translate"):
        if source_code_snippet.strip():
            with st.spinner("Translating code..."):
                try:
                    translated_code = translate_code(source_code_snippet, target_language)
                    # print(translated_code)
                    print(extractCode(translated_code))
                    st.success("Code translation complete!")
                    st.markdown(translated_code)
                except Exception as e:
                    st.error(f"Error translating code: {e}")
        else:
            st.error("Please enter a code snippet.")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) < 3 or sys.argv[1] == "help" :
        print("Usage: [Target Language] [Input File] [Output File]")
        print("Languages: \n")
        for i in languages:
            print(f"[>] {i}")
    elif sys.argv[1].title() in languages:
        commandLine(sys.argv[1])
    