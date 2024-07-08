# CodeXchange: Pilot/Setup

## 1. Cloning the Repository

The first step is to clone the repository:

```sh
git clone "https://github.com/nilakshkashyap/Code-Translator.git"
cd Code-Translator
```
This creates a copy where one can run and edit the code files.

## 2. Installing Dependencies

Before running the files all the dependencies must be installed, these have been specified in the **"requirements.txt"** file. This can be done using the following command:

```sh
pip install -r requirements.txt
```
This should be enough to install the dependencies but you can recheck whether all of the libraries have been installed by using the command: 

```sh
pip freeze
```
Compare the libraries shown with the ones in **"requirements.txt"**

## 3. Running the Streamlit web-app

All that is left is to run the Streamlit Web-App, this can be done by using the following command:

```terminal
streamlit run app.py
```

### Now Enter your Code and translate!