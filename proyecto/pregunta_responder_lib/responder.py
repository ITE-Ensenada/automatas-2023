import spacy

nlp = spacy.load("es_core_news_md")

def responder_pregunta(pregunta_usuario, respuestas):
    if pregunta_usuario is None:
        return "La pregunta no puede estar vacía"

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

    return respuesta
