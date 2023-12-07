from bs4 import BeautifulSoup

with open("html/oferta-educativa/extension-playas-de-rosarito-ite/ingenieria-electromecanica-extension-playas-de-rosarito.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'table'])
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

# Encontrar enlaces de descarga
download_links = soup.find_all('a', href=True)  # Encuentra todos los elementos 'a' con un atributo href

# Filtrar enlaces de descarga por la extensión del archivo
allowed_extensions = ('.pdf', '.doc', '.docx','.zip')  
for link in download_links:
    href = link.get('href')
    if any(ext in href for ext in allowed_extensions):
        print("Link de Descarga:", href)
