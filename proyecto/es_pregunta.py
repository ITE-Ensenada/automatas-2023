from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from preguntas import preguntas

flattened_questions = ["".join(question) for question_set in preguntas for question in question_set]
labels = ["Class1"] * len(preguntas[0]) + ["Class2"] * len(preguntas[1])
X_train, X_test, y_train, y_test = train_test_split(flattened_questions, labels, test_size=0.2)


# Convert text data to feature vectors using CountVectorizer
vectorizer = CountVectorizer()
vectorizer.fit_transform(X_train)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Create and train classifier
clf = MultinomialNB()
clf.fit(X_train_vectorized, y_train)

# Predict
predictions = clf.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")



single_sentence = ["Quien es la coordinadora de sistemas?"]
single_sentence_vectorized = vectorizer.transform(single_sentence)

# Make predictions on the single sentence
prediction_single_sentence = clf.predict(single_sentence_vectorized)
print(f"Prediction for the single sentence: {prediction_single_sentence[0]}")


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