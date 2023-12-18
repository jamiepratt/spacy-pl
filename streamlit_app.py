# streamlit_app.py
import spacy_streamlit
import spacy.cli

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "Sundar Pichai is the CEO of Google."

# Download the language model if not already installed
for model in models:
    if not spacy.util.is_package(model):
        spacy.cli.download(model)

spacy_streamlit.visualize(models, default_text)