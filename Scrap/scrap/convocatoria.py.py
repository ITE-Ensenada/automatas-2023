from bs4 import BeautifulSoup

with open("html/estudiantes/convocatoria/estudiantes.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

elements = soup.find_all(['p', 'h1', 'h2'])
for element in elements:
    text = element.text.strip()
    # Encontrar y eliminar SPAM
    spam_frases = [
        "Me gusta enFacebook",
        "Síguenos enTwitter",
        "Síguenos enYouYube",
        "Síguenos enInstagram",
        "Manda un mensaje porWhatsApp"
    ]
    if not any(spam_frase in text for spam_frase in spam_frases):
        print(text)
