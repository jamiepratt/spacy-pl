# streamlit_app.py
import spacy_streamlit
models = [
    "pl_core_news_sm",
    "ca_core_news_sm",
    "da_core_news_sm",
    "de_core_news_sm",
    "el_core_news_sm",
    "en_core_web_sm",
    "es_core_news_sm",
    "fi_core_news_sm",
    "fr_core_news_sm",
    "hr_core_news_sm",
    "it_core_news_sm",
    "ja_core_news_sm",
    "ko_core_news_sm",
    "lt_core_news_sm",
    "mk_core_news_sm",
    "nb_core_news_sm",
    "nl_core_news_sm",
    "pt_core_news_sm",
    "ro_core_news_sm",
    "sl_core_news_sm",
    "sv_core_news_sm",
    "ru_core_news_sm",
    "uk_core_news_sm",
    "xx_ent_wiki_sm",
    "xx_sent_ud_sm",
    "zh_core_web_sm"]

default_text = "Marta poszła spać. Była jedenasta wieczorem. Ona wyłączyła światło i położyła się do łóżka. W pokoju było ciemno i cicho. Marta próbowała usnąć, ale nie mogła."

spacy_streamlit.visualize(models, default_text)