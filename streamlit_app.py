# streamlit_app.py
import spacy_streamlit
import spacy.cli
import spacy.util

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "Sundar Pichai is the CEO of Google."

# Create a virtual environment
venv_path = "/app/.venv"
spacy.util.set_env("VIRTUAL_ENV", venv_path)

# Download the language model if not already installed
for model in models:
    if not spacy.util.is_package(model):
        spacy.cli.download(model)

spacy_streamlit.visualize(models, default_text)