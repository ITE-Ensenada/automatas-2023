# BOT DE TELEGRAM QUIZ DE POKEMON

Link: [https://github.com/ITE-Ensenada/backend-20231/blob/Salazar/design-doc.md](#)

Author(s): Juan Carlos Salazar Silva

Status: [Reviewed]

Última actualización: 2023-10-04

## Contenido
- Objetivo
- Reglas del juego
- Características
- Diseño Detallado
  - Frontend
  - Backend
- Consideraciones

## Objetivo
Crear un bot de Telegram que permita a los usuarios jugar un quiz de Pokémon, donde deben adivinar el nombre del Pokémon basado en una imagen y recibir retroalimentación sobre sus respuestas.

## Reglas del juego
1. El bot enviará una imagen de un Pokémon al usuario.
2. El usuario debe adivinar el nombre del Pokémon en un tiempo limitado.
3. El usuario puede proporcionar su respuesta en texto.
4. El bot verificará la respuesta del usuario y proporcionará retroalimentación.
5. El usuario acumulará puntos por respuestas correctas.
6. El usuario puede ver su puntuación actual en cualquier momento.
7. Despues de 30 segundos de inactividad el quiz se finalizara.

## Características
- Sistema de puntuación.
- Temporizador para limitar el tiempo de respuesta.
- Amplia base de datos de imágenes de Pokémon.
- Retroalimentación inmediata después de cada respuesta.
- Comandos de inicio y ayuda.

## Diseño Detallado
### Frontend
El frontend del bot de Telegram consistirá en la interfaz de usuario que interactúa con los usuarios a través de mensajes de Telegram. Deberá proporcionar las siguientes funcionalidades:

- Comando "/start" para iniciar el juego.
- Comando "/help" para obtener comandos del bot.
- Comando "/rules" para obtener instrucciones y reglas del juego.
- Comando "/pokedex" para obtener lista de pokemons en el juego.
- Comando "/stop" termina el juego.
- Comando "/About" para obtener informacion acerca del bot.
- Envío de imágenes de Pokémon a los usuarios.
- Recepción de respuestas de los usuarios en forma de texto.

### Backend
El backend del bot de Telegram se encargará de gestionar el juego, verificar respuestas, llevar un registro de la puntuación y enviar retroalimentación. Deberá proporcionar las siguientes funcionalidades:

- Base de datos que almacena información sobre Pokémon, incluyendo imágenes y nombres.
- Temporizador para limitar el tiempo de respuesta del usuario.
- Lógica para verificar si las respuestas del usuario son correctas.
- Sistema de puntuación que registra y actualiza la puntuación del usuario.
- Generación de imágenes aleatorias de Pokémon para cada pregunta.
- Envío de mensajes de retroalimentación al usuario después de cada respuesta.

## Consideraciones
- Se puede considerar trabajar con una base de datos para almacenar imagenes y nombres a una mayor escala.
- Se debe manejar la interacción con múltiples usuarios de forma simultánea.
- Se debe garantizar que el bot sea fácil de usar y proporcione instrucciones claras.

Este diseño proporciona una visión general de cómo se podría desarrollar un bot de Telegram para un juego de quiz de Pokémon. Los detalles específicos de la implementación pueden variar según las preferencias y recursos disponibles del desarrollador.

## Solución 2
Podemos reusar los mismos métodos de la solución 1, con los siguientes cambios.

### Aplicar el quiz con un bot de discord
En lugar de usar un bot de Telegram se usaría uno de Discord. Esto necesitaría otro design doc enfocado a la solución 2, si se elige esta solución.

## Consideraciones
- La librería solo está en Python. Tal vez podemos entender cómo funciona para implementarla por nuestra cuenta en otro lenguaje si es necesario.
