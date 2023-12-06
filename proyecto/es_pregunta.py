def es_pregunta(input_usuario):
    """
    Determina si el parametro ingresado es una pregunta y clasifica el tipo de pregunta.
    1: si es una pregunta con pronombres interrogativos.
    2: si es una pregunta con adjetivos interrogativos.
    3: si es una pregunta con adverbios interrogativos.
    4: si es una pregunta con partículas interrogativas.
    5: si es una pregunta específica con "por qué".
    """

    # Listas de palabras interrogativas
    pronombres_interrogativos = ['quien', 'que', 'cual', 'cuales', 'cuanto', 'cuantos', 'cuanta', 'cuantas', 'cuando', 'donde', 'por que', 'como']

    adjetivos_interrogativos = ['que', 'cual', 'cuales', 'cuanto', 'cuantos', 'cuanta', 'cuántas']

    adverbios_interrogativos = ['cuando', 'por que', 'como']

    particulas_interrogativas = ["no", "acaso", "verdad", "a que", "o no", "no es cierto", "no es verdad", "no es asi"]

    # Convierte en minúsculas el prompt
    input_usuario = input_usuario.lower()

    # Divide el texto ingresado por el usuario en palabras y se asigna a la variable palabras
    palabras = input_usuario.split()

    # Banderas para el tipo de pregunta
    bandera = 0
    palabra_interrogativa = None  # Aqui se guargara la palabra para despues se muestre en la salida de la solicitud
    tipo_pregunta = None  # Agregamos una variable para el tipo de pregunta

    # Verificar las palabras que hacen que el texto sea pregunta
    for palabra in palabras:
        if palabra in pronombres_interrogativos:
            bandera = 1  # Pregunta pronombres interrogativa
            palabra_interrogativa = palabra  # la palabra que toma el for se almacena en la palabra interrogativa
            tipo_pregunta = "pronombres_interrogativos"
            return bandera, palabra_interrogativa, tipo_pregunta  # Regresamos la tipo de pregunta, la palabra, y a que interrogativa se encuentra la palabra

        elif palabra in adjetivos_interrogativos:
            bandera = 2  # Pregunta Adjetivos Interrogativos
            palabra_interrogativa = palabra  # la palabra que toma el for se almacena en la palabra interrogativa
            tipo_pregunta = "adjetivos_interrogativos"
            return bandera, palabra_interrogativa, tipo_pregunta  # Regresamos la tipo de pregunta, la palabra, y a que interrogativa se encuentra la palabra

        elif palabra in adverbios_interrogativos:
            bandera = 3  # Pregunta Adverbios Interrogativos
            palabra_interrogativa = palabra  # la palabra que toma el for se almacena en la palabra interrogativa
            tipo_pregunta = "adverbios_interrogativos"
            return bandera, palabra_interrogativa, tipo_pregunta  # Regresamos la tipo de pregunta, la palabra, y a que interrogativa se encuentra la palabra

        elif palabra in particulas_interrogativas:
            bandera = 4  # Pregunta Particulas interrogativas
            palabra_interrogativa = palabra  # la palabra que toma el for se almacena en la palabra interrogativa
            tipo_pregunta = "particulas_interrogativas"
            return bandera, palabra_interrogativa, tipo_pregunta  # Regresamos la tipo de pregunta, la palabra, y a que interrogativa se encuentra la palabra

        elif "por" in palabra and "que" in palabra and palabra[palabra.index("por") + 1] == "que":
            bandera = 5
            palabra_interrogativa = palabra
            tipo_pregunta = "por_que"
            return bandera, palabra_interrogativa, tipo_pregunta

    return bandera, palabra_interrogativa, tipo_pregunta  # No es una pregunta
