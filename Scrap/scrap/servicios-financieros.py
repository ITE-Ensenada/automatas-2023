from bs4 import BeautifulSoup

with open("html/estudiantes/servicios-financieros/procedimiento-para-pago-de-ficha-examen-seleccion-curso-preparatorio-inscripcion-de-nuevo-ingreso-reinscripcion-servicios-y-solicitud-de-facturacion.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

# Buscar elementos de texto
elements = soup.find_all(['p', 'h1', 'h2', 'h3'])
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
