import spacy

nlp = spacy.load("es_core_news_md")
"""
respuestas = {
    ///GENERALES
    "1": '¿Dónde puedo consultar mi kardex?',
    "2": '¿Dónde puedo revisar mi horario?',
    "3": '¿Quién es mi coordinador?',
    "4": '¿Donde tramitar la credencial estudiantil?',
    "5": '¿Qué requisitos se requieren para realizar el servicio social?'
    "Donde puedo reportar algo que perdi/encontre"
    "Cuales/cuando son las fechas de recuperacion"
    "cuando son vacaciones"
    "Que especialidades existen/hay/o tiene la carrera de XXXX"
    "horario de la biblioteca"
    "donde reviso mis calificaciones"
    "cuando entramos"
    "horario de la cafeteria"
    "horario de las coordinaciones/servicio" //especifica
    "horario de la escuela"
    "donde esta el laboratorio X"
    "donde esta posgrado y que posgrados tiene el ITE"
    "Cuales son los costos, o cuanto cuesta un semestre"
    "donde esta enfermeria"
    "como doy de baja un materia"
    "como me cambio de carrera"
    "como o donde cambio la clave de mi correo institucional"
    "como pagar la inscripcion / donde como y porque"
    "que becas hay"
    ""








    ,
}
"""
def responder_pregunta(pregunta_usuario):
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
