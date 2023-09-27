from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

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
