import spacy
from flask import Flask, request, jsonify

# Cargar el modelo de lenguaje en español de spaCy
nlp = spacy.load("es_core_news_md")

respuestas = {
    "1": '¿Dónde puedo consultar mi kardex?',
    "2": '¿Dónde puedo revisar mi horario?',
    "3": '¿Quién es mi coordinador?',
    "4": '¿Documentos para tramitar la credencial estudiantil?',
    "5": '¿Qué requisitos se requieren para realizar el servicio social?',
}

app = Flask(__name__)

@app.route('/pregunta', methods=['POST'])
def responder_pregunta():
    data = request.get_json()
    pregunta_usuario = data.get("pregunta")

    if pregunta_usuario is None:
        return jsonify({"respuesta": "La pregunta no puede estar vacía"})

    mejor_similitud = -1
    mejor_respuesta_id = None

    for respuesta_id, respuesta_texto in respuestas.items():
        if respuesta_texto is not None:
            similitud = nlp(pregunta_usuario).similarity(nlp(respuesta_texto))
            if similitud > mejor_similitud:
                mejor_similitud = similitud
                mejor_respuesta_id = respuesta_id

    if mejor_respuesta_id:
        respuesta = respuestas[mejor_respuesta_id]
    else:
        respuesta = "Lo siento, no tengo una respuesta para esa pregunta."

    return jsonify({"respuesta": respuesta})


if __name__ == '__main__':
    app.run(debug=True)
