from bs4 import BeautifulSoup

with open("html/estudiantes/servicios-estudiantiles/kardex.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

# Buscar elementos de texto
elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'li'])
for element in elements:
    # Verificar si esta ligado a un <nav> para omitir todos los <li> dentro 
    if element.name == 'li' and element.find_parent('nav'):
        continue

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

# Obtener links de imagen y filtrar los enlaces no deseados``
image_tags = soup.find_all('img')
spam_links = [
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/logo-educacion.svg",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/logo-ensenada.png",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/linea-vertical-separador-logos.svg",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/logo-tecnm.svg",
    "/wp-content/themes/tecnm/images/instagram.png",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/linea-vertical-separador-logos.svg",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/correo-icono.png",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/correo-icono.png",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/LogoTecNM Blanco.png",
    "ttps://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/house-white.png",
    "https://tijuana.tecnm.mx/wp-content/themes/tecnm/images/house-black.png",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/fb_new.png",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/youtube.png",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/twitt_new.png",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/house-white.png",
    "https://www.ensenada.tecnm.mx/wp-content/themes/tecnm/images/Whatsapp.png"
]

for img in image_tags:
    if 'src' in img.attrs:
        image_source = img['src']
        if image_source not in spam_links:
            print("Link:", image_source)
