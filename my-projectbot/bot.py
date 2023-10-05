#!/usr/bin/env python
# pylint: disable=unused-argument, import-error
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import asyncio
import logging

from telegram import ForceReply, Update, InlineKeyboardButton,InlineKeyboardMarkup, InputFile
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    keyboard = [
        InlineKeyboardButton("Numeros", callback_data="1"),
        InlineKeyboardButton("Operaciones Basicas", callback_data="2"),
    ],


    [InlineKeyboardButton("Opcion 3", callback_data="3")],

    reply_markup= InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Hola! Mi nombre es Profesor bot, Que te gustaria aprender?", reply_markup=reply_markup)

    #user = update.effective_user
    #await update.message.reply_html(
        #rf"Hi {user.mention_html()}!",
        
    #)

async def image_resta(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    image_path = 'C:/backend-20231/my-projectbot/Img/resta.jpg'
    caption = 'Si tengo 5 manzanas en una cesta, y quito 2, dentro de la cesta me quedarán 3 manzanas. es decir que 5 menos 2 es igual a 3.'

    try:
        with open(image_path, 'rb') as photo_file:
            await context.bot.send_photo(chat_id=chat_id, photo=InputFile(photo_file), caption=caption),
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text='No se puede cargar la image {str(e)}')

async def image_suma(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    image_path = 'C:/backend-20231/my-projectbot/Img/suma.jpg'
    caption = 'Si tengo 2 manzanas verdes y 3 manzanas rojas, y quiero saber cuántas manzanas tengo en total, junto todas las manzanas en un solo cesto y las cuento: tengo 5 manzanas en total, por lo tanto 2 + 3  es igual a 5.'

    try:
        with open(image_path, 'rb') as photo_file:
            await context.bot.send_photo(chat_id=chat_id, photo=InputFile(photo_file), caption=caption),
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text="No se puede cargar la image {str(e)}")

async def send_image(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    image_path = 'C:/backend-20231/my-projectbot/Img/operaciones.jpg'
    caption = 'Hola bienvenido al area de operaciones aritmeticas, Que leccion deseas aprender?'

    keyboard = [[InlineKeyboardButton("Suma", callback_data="seccion_1"),
                InlineKeyboardButton("Resta", callback_data="seccion_2")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        with open(image_path, 'rb') as photo_file:
            await context.bot.send_photo(chat_id=chat_id, photo=InputFile(photo_file), caption=caption, reply_markup=reply_markup)
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text="No se pudo cargar la imagen: {str(e)}")

imagenes = [
    'C:/backend-20231/my-projectbot/Img/num1.jpg',
    'C:/backend-20231/my-projectbot/Img/num2.jpg',
    'C:/backend-20231/my-projectbot/Img/num3.jpg',
    'C:/backend-20231/my-projectbot/Img/num4.jpg',
    'C:/backend-20231/my-projectbot/Img/num5.jpg'
]

imagenes_leccion_2 = [
    'C:/backend-20231/my-projectbot/Img/num1obj.jpg',
    'C:/backend-20231/my-projectbot/Img/num2obj.jpg',
    'C:/backend-20231/my-projectbot/Img/num3obj.jpg',
    'C:/backend-20231/my-projectbot/Img/num4obj.jpg',
    'C:/backend-20231/my-projectbot/Img/num5obj.jpg'
]

async def enviar_imagenes_leccion_2(update, context):
    chat_id = update.effective_chat.id
    for imagen_path in imagenes_leccion_2:
        with open(imagen_path, 'rb') as photo_file:
            await context.bot.send_photo(chat_id=chat_id, photo=InputFile(photo_file))
        await asyncio.sleep(10)

async def enviar_imagenes_separadas(update, context):
    chat_id = update.effective_chat.id
    for imagen_path in imagenes:
        with open(imagen_path, 'rb') as photo_file:
            await context.bot.send_photo(chat_id=chat_id, photo=InputFile(photo_file))
        await asyncio.sleep(10)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    data = query.data

    if data == "1":
        lecciones = [
            [InlineKeyboardButton("Contar", callback_data="leccion_1")],
            [InlineKeyboardButton("Contar con objetos", callback_data="leccion_2")]
        ]
        reply_markup = InlineKeyboardMarkup(lecciones)
        await query.edit_message_text("Muy bien vamos a comenzar con la leccion de Numeros \n\n" "Los numeros son palabras especiales que usamos para contar cosas, como juguetes, amigos o galletas.",reply_markup=reply_markup)
    elif data == "leccion_1":
        await enviar_imagenes_separadas(update, context)
    elif data == "leccion_2":
        await enviar_imagenes_leccion_2(update, context)
    elif data == "seccion_1":
        ejemplo = [
            [InlineKeyboardButton("Ejemplo", callback_data="ejemplos")]
        ]
        reply_markup = InlineKeyboardMarkup(ejemplo)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Sumar es juntar dos o más cosas en un grupo, para saber cuántas hay en total \n\n" "Si te sientes perdido solo haz click en el siguiente boton", reply_markup=reply_markup)   
    elif data == "ejemplos":
        await image_suma(update, context)
    elif data == "seccion_2":
        resta = [
            [InlineKeyboardButton("Ejemplo", callback_data="ejemplos_resta")]
        ]
        reply_markup = InlineKeyboardMarkup(resta)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Restar es quitar una cierta cantidad a otra que ya teníamos \n\n' 'Si te sientes perdido solo haz click en el siguiente boton', reply_markup=reply_markup)
    elif data == "ejemplos_resta":
        await image_resta(update, context)
    elif data == "2":
        keyboard = [[InlineKeyboardButton("mostrar imagen", callback_data="show_image")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Haz clic en el boton para mostrar la imagen:", reply_markup=reply_markup)
    elif data == "show_image":
        await send_image(update, context)
    #await query.answer()
    
    #await query.edit_message_text(text=f"Selected option {query.data}")



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


#async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #"""Echo the user message."""

    #await update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6558167523:AAEW-EF0a0an16sTOxuWUVppXMH-noewJZY").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()