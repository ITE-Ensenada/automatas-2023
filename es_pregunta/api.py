# Primero, importamos las herramientas que necesitamos.
from flask import Flask, request, jsonify

# Importo la función creada en es_pregunta.py para ayudarnos a responder preguntas.
from es_pregunta import es_pregunta

# Creamos la api usando Flask.
app = Flask(__name__)

# Se le dice a la api qué hacer cuando alguien visita la dirección principal ("/").
@app.route('/', methods=['POST'])
def analizar_pregunta():
    # Aquí, tomamos la pregunta que la persona escribió en el bot.
    pregunta = request.args.get('pregunta', '')

    # "es_pregunta" para ver si la pregunta es de verdad una pregunta.
    resultado, palabra_interrogativa, tipo_pregunta = es_pregunta(pregunta)

    # Ahora, dependiendo de lo que encontramos al analizar la pregunta, se prepara una respuesta.
    if resultado != 0:
        # Si la pregunta es real, se imprime lo siguiente.
        respuesta = {
            'Es pregunta': f'"{pregunta}"',
            'Palabra': f'"{palabra_interrogativa}"',
            'Tipo de Pregunta Detallado': f'"{tipo_pregunta}, {resultado}"'
        }
    else:
        # Si la pregunta no es real, decimos que no es una pregunta.
        respuesta = {
            'Es pregunta': f'"{pregunta}"',
            'Palabra': '',
            'Tipo de Pregunta': 'No es una pregunta'
        }

    # Finalmente, la respuesta se convierte en un formato JSON 
    return jsonify(respuesta)

# La api esta lista
if __name__ == '__main__':
    app.run(debug=True)
