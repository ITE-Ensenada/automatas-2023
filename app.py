from flask import Flask
# Crea una instancia de la aplicación Flask
app = Flask(__name__)

##
# Inicializa las puntuaciones
score_bad = 0
escolares = 0
biblioteca = 0
cafeteria = 0
asesores = 0

# Palabras que restan puntos
mala_palabras = ["puto", "tonto", "wey"]  # Resta 1 punto
no_eticas = ["joto", "negro", "indio", "pendejo"]  # Resta 2 puntos

# Palabras que suman puntos según la categoría
palabras_triggers = {
    'kardex': escolares + 1,
    'libros': biblioteca + 1,
    'boleta': escolares + 1,
    'estudiar': biblioteca + 1,
    'comida': cafeteria + 1,
    'tutor': asesores + 1,
    'asesor': asesores + 1,
}

# Palabras que restan puntos según la categoría
medium_bad_words = {
    'puto': -1,
    'guey': -2,
    'pendejo': -1,
}

# Define una ruta y una función para manejarla
@app.route('/')
def index():
    return '¡Hola, mundo! Esta es mi primera aplicación Flask.'

# Define otra ruta y función
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return f'Hola, {nombre}!'

# Ejecuta la aplicación si se ejecuta este archivo
if __name__ == '__main__':
    app.run()
