import spacy 

# Cargar el modelo de lenguaje en español de spaCy
nlp = spacy.load("es_core_news_md")

respuestas = {
    "1": '¿Dónde puedo consultar mi kardex?',
    "2": '¿Dónde puedo revisar mi horario?',
    "3": '¿Quién es mi coordinador?',
    "4": '¿Documentos para tramitar la credencial estudiantil?',
    "5": '¿Qué requisitos se requieren para realizar el servicio social?',
}

while True:
    pregunta_usuario = input("Hazme una pregunta (o escribe 'salir' para terminar): ")

    if pregunta_usuario.lower() == "salir":
        break

    mejor_similitud = -1
    mejor_respuesta_id = None

    for respuesta_id, respuesta_texto in respuestas.items():
        similitud = nlp(pregunta_usuario).similarity(nlp(respuesta_texto))
        if similitud > mejor_similitud:
            mejor_similitud = similitud
            mejor_respuesta_id = respuesta_id

    if mejor_respuesta_id:
        respuesta = respuestas[mejor_respuesta_id]
    else:
        respuesta = "Lo siento, no tengo una respuesta para esa pregunta."

    print("Respuesta:", respuesta)
