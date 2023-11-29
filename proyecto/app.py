from flask import Flask, request, jsonify
from pregunta_responder_lib.responder import responder_pregunta

app = Flask(__name__)

respuestas = {
    "1": '¿Dónde puedo consultar mi kardex?',
    "2": '¿Dónde puedo revisar mi horario?',
    "3": '¿Quién es mi coordinador?',
    "4": '¿Documentos para tramitar la credencial estudiantil?',
    "5": '¿Qué requisitos se requieren para realizar el servicio social?',
}

@app.route('/pregunta', methods=['POST'])
def responder_pregunta_route():
    data = request.get_json()
    pregunta_usuario = data.get("pregunta")

    if pregunta_usuario is None:
        return jsonify({"respuesta": "La pregunta no puede estar vacía"})

    respuesta = responder_pregunta(pregunta_usuario, respuestas)

    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(debug=True)
