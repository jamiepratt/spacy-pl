# streamlit_app.py
import spacy_streamlit

models = ["pl_core_news_sm", "pl_core_news_md"
            "en_core_web_sm", "en_core_web_md"]
default_text = "Marta poszła spać. Była jedenasta wieczorem. Ona wyłączyła światło i położyła się do łóżka. W pokoju było ciemno i cicho. Marta próbowała usnąć, ale nie mogła."

spacy_streamlit.visualize(models, default_text)