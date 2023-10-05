import spacy
from flask import Flask
# Crea una instancia de la aplicación Flask
app = Flask(__name__)
nlp = spacy.load("es_core_news_sm")


texto = "SpaCy es una excelente herramienta de procesamiento de lenguaje natural."
doc = nlp(texto)

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_)

