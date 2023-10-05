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

async def send_image_with_text(update: Update, context: CallbackContext) -> None:
    image_path='Img/R.jpg'

    try:
        await update.callback_query.message.reply_photo(
            photo=InputFile(image_path),
            caption='Aqui tienes un ejemplo'
    )
    except Exception as e:
        await update.callback_query.message.reply_text(f"Error: {str(e)}")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    data = query.data

    if data == "1":
        await query.edit_message_text("Muy bien vamos a comenzar con la leccion de Numeros \n\n" "Los numeros son palabras especiales que usamos para contar cosas, como juguetes, amigos o galletas.")
    elif data == "2":
        await send_image_with_text(update, context)
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