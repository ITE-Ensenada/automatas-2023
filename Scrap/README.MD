# Documento de Diseño: Web Scraping para el Instituto Tecnológico de Ensenada

Enlace: [https://github.com/Fuanchitos/ITE-Backend-I-Scraping/blob/main/README.MD](#)

Autor(es): Juan Carlos Salazar Silva

Estado: [En Revisión]

Última Actualización: 2023-11-14

## Instalacion
1. Instalar python 3.11.4
2. Opcion 1 
   Instalar la libreria de BeautifulSoup4 "BS4"
   con pip install bs4
3. Listo para usar los codigos de scrap

4. Opcion 2
5. Utilizar el comando pip freeze > requirements.txt
6. Listo para usar los codigos de scrap

## Instrucciones de Uso
1. Tener instalado las librerias "BS4"
2. Abrir la carpeta "scraps".
3. Elige un archivo .py, ya que cada uno hace referencia a una sección de la página del Instituto Tecnológico de Ensenada.
4. Utiliza los nombres y rutas de los archivos HTML para realizar el scraping
   por ejemplo: 
   with open("html/oferta-educativa/posgrados/doctorado-en-ciencias-en-ingenieria-mecatronica.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser').
5. En este caso estas utilizando el scrap para el apartado oferta-educativa/posgrados/, solo se actualizara el ultimo nombre.

## Contenidos
- Objetivo
- Metas
- No Objetivos
- Contexto
- Visión General
- Diseño Detallado
  - Scraping de Páginas del Instituto Tecnológico de Ensenada
    - Obtención de Párrafos
    - Extracción de Títulos
    - Recopilación de Tablas
- Consideraciones

## Metas
Crear un script en Python para hacer scraping en las páginas web del Instituto Tecnológico de Ensenada, extrayendo información clave como párrafos, títulos y tablas.

El objetivo es obtener datos relevantes de las páginas del Instituto para un análisis posterior o para integrar la información en otras aplicaciones.

## Objetivos
- Extraer párrafos informativos
- Recopilar títulos de secciones importantes
- Obtener datos estructurados de tablas específicas
- Ignorar palabras que son innecesarias al recopilar información

## No Objetivos
- Realizar acciones invasivas en las páginas web del Instituto
- Acceder a áreas restringidas o protegidas por autenticación

## Contexto
El Instituto Tecnológico de Ensenada es una institución educativa con información relevante en sus páginas web. El propósito es acceder a esta información de manera automatizada para diversos propósitos, como análisis de datos o visualización.

## Visión General
Para el scraping de las páginas del Instituto Tecnológico de Ensenada, se utilizará Python junto con la biblioteca BeautifulSoup para analizar la estructura HTML y obtener datos específicos como párrafos, títulos y tablas.

## Detailed Design

### Scraping de Páginas del Instituto Tecnológico de Ensenada

#### Obtención de Párrafos
- Se identificarán y extraerán los párrafos informativos de las páginas relevantes del Instituto.

#### Extracción de Títulos
- Se buscarán y obtendrán los títulos de las secciones importantes para comprender la estructura y el contenido de las páginas.

#### Recopilación de Tablas
- Se analizarán y extraerán datos estructurados de las tablas disponibles en las páginas del Instituto.

## Consideraciones
- Respetar los términos de uso del sitio web del Instituto Tecnológico de Ensenada.
- Evitar realizar solicitudes excesivas para no sobrecargar el servidor.
- Asegurar que el scraping se realice de manera ética y legal.
