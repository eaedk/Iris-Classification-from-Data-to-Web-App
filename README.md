# Iris-Classification-from-Data-to-Web-App

## Setup

To setup this project, you need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's `root :: repo_name> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## Execution

- Run the Streamlit app (being at the repository root):

        streamlit run src/streamlit_app.py

- Go to your browser at the following address :
        
    http://localhost:8501