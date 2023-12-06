#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from typing import Dict

from telegram import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


# Main states
MAIN_MENU, SUB_MENU, END_ROUTES = range(3)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    keyboard = [
        [
            InlineKeyboardButton(" Sistemas 🖥️", callback_data="sistemas"),
            InlineKeyboardButton(" Innovación Agrícola  🌾", callback_data="agricola"),
        ],
        [
            InlineKeyboardButton(
                " Electromecánica ⚙️", callback_data="electromecanica"
            ),
            InlineKeyboardButton(" Gestión Empresarial 📈", callback_data="gestion"),
        ],
        [
            InlineKeyboardButton(" Industrial 🏭", callback_data="industrial"),
            InlineKeyboardButton(" Mecatrónica 🤖", callback_data="mecatronica"),
        ],
        [
            InlineKeyboardButton(" Administración 📊", callback_data="admin"),
            InlineKeyboardButton(" Electrónica 📡", callback_data="electronica"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Elige una Ingeniería", reply_markup=reply_markup)

    return MAIN_MENU


async def show_submenu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton("Noticias 📰", callback_data="noticias"),
            InlineKeyboardButton("Escolares 🎒", callback_data="escolares"),
        ],
        [
            InlineKeyboardButton("Carreras 🎓", callback_data="carreras"),
            InlineKeyboardButton("Mapas 🗺️", callback_data="mapas"),
        ],
        [
            InlineKeyboardButton("Horario ⏰", callback_data="horario"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Editar el mensaje original con el submenu
    await query.edit_message_text(
        text="Selecciona una opción de tu interés", reply_markup=reply_markup
    )

    # Cambiar a la etapa SUB_MENU
    return SUB_MENU


async def handle_submenu_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    chosen_option = query.data

    match chosen_option:
        case "noticias":
            print("notifififi")
            pass
        case "carreras":
            pass
        case "mapas":
            pass
        case "escolares":
            pass
        case "horario":
            pass
    # Editar el mensaje original con la opción seleccionada del submenu
    await query.edit_message_text(text=f"Selected option in submenu: {chosen_option}")

    # Cambiar a la etapa END_ROUTES
    return END_ROUTES


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(text="See you next time!")

    return ConversationHandler.END


def main() -> None:
    application = (
        Application.builder()
        .token("6332760312:AAE7kTnvUPO1mdqtfZR22v3uVG5ueLbUXG0")
        .build()
    )

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("iniciar", start)],
        states={
            MAIN_MENU: [CallbackQueryHandler(show_submenu)],
            SUB_MENU: [
                CallbackQueryHandler(handle_submenu_choice),
            ],
            END_ROUTES: [CommandHandler("adios", start)],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
