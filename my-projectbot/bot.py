#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler

# Configurar el sistema de registro para mostrar mensajes informativos
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# Establecer un nivel de registro más alto para httpx para evitar el registro de todas las solicitudes GET y POST
logging.getLogger("httpx").setLevel(logging.WARNING)

# Obtener un objeto de registro para este módulo
logger = logging.getLogger(__name__)

# Definir las etapas de la conversación
MAIN_MENU, SUB_MENU, END_ROUTES = range(3)
# Definir los datos de devolución de llamada (callback data)
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT = range(8)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Enviar un mensaje en `/start`."""
    # Obtener información del usuario que inició la conversación
    user = update.message.from_user
    # Registrar el inicio de la conversación en el sistema de registro
    logger.info("User %s started the conversation.", user.first_name)

    # Definir el teclado principal con botones para cada opción de ingeniería
    keyboard = [
        [
            InlineKeyboardButton(" Sistemas 🖥️", callback_data=str(ONE)),
            InlineKeyboardButton(" Innovación Agrícola  🌾", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton(" Electromecánica ⚙️", callback_data=str(THREE)),
            InlineKeyboardButton(" Gestión Empresarial 📈", callback_data=str(FOUR)),
        ],
        [
            InlineKeyboardButton(" Industrial 🏭", callback_data=str(FIVE)),
            InlineKeyboardButton(" Mecatrónica 🤖", callback_data=str(SIX)),
        ],
        [
            InlineKeyboardButton(" Administración 📊", callback_data=str(SEVEN)),
            InlineKeyboardButton(" Electrónica 📡", callback_data=str(EIGHT)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Enviar el mensaje con el teclado principal
    await update.message.reply_text("Elige una Ingeniería", reply_markup=reply_markup)

    # Cambiar a la etapa MAIN_MENU
    return MAIN_MENU


async def show_submenu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # Manejar la selección del teclado principal y mostrar el submenu correspondiente
    query = update.callback_query
    await query.answer()

    # Definir el teclado del submenu con opciones específicas
    keyboard = [
       [
        InlineKeyboardButton("Noticias 📰", callback_data="1"),
        InlineKeyboardButton("Escolares 🎒", callback_data="2"),
    ],
    [
        InlineKeyboardButton("Carreras 🎓", callback_data="3"),
        InlineKeyboardButton("Mapas 🗺️", callback_data="4"),
    ],
    [
        InlineKeyboardButton("Horario ⏰", callback_data="5"),
       
    ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Editar el mensaje original con el submenu
    await query.edit_message_text(text="Selecciona una opción de tu interés", reply_markup=reply_markup)
    
    # Cambiar a la etapa SUB_MENU
    return SUB_MENU


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # Reiniciar la conversación y mostrar nuevamente el teclado principal
    query = update.callback_query
    await query.answer()

    # Definir el teclado principal al reiniciar
    keyboard = [
        [
            InlineKeyboardButton("Sistemas Computacionales 🖥️", callback_data=str(ONE)),
            InlineKeyboardButton("Innovación Agrícola Sustentable 🌾", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton(" Electromecánica ⚙️", callback_data=str(THREE)),
            InlineKeyboardButton(" en Gestión Empresarial 📈", callback_data=str(FOUR)),
        ],
        [
            InlineKeyboardButton(" Industrial 🏭", callback_data=str(FIVE)),
            InlineKeyboardButton(" Mecatrónica 🤖", callback_data=str(SIX)),
        ],
        [
            InlineKeyboardButton("Licenciatura en Administración 📊", callback_data=str(SEVEN)),
            InlineKeyboardButton(" Electrónica 📡", callback_data=str(EIGHT)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Editar el mensaje original con el teclado reiniciado
    await query.edit_message_text(text="Start handler, Choose a route", reply_markup=reply_markup)
    
    # Cambiar a la etapa MAIN_MENU
    return MAIN_MENU


async def handle_submenu_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # Manejar la selección de opciones del submenu y mostrar el resultado
    query = update.callback_query
    await query.answer()

    chosen_option = query.data
    # Editar el mensaje original con la opción seleccionada del submenu
    await query.edit_message_text(text=f"Selected option in submenu: {chosen_option}")

    # Cambiar a la etapa END_ROUTES
    return END_ROUTES


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # Finalizar la conversación y despedirse del usuario
    query = update.callback_query
    await query.answer()

    # Editar el mensaje original con el mensaje de despedida
    await query.edit_message_text(text="See you next time!")
    
    # Finalizar la conversación
    return ConversationHandler.END


def main() -> None:
    # Crear una instancia de la aplicación de Telegram
    application = Application.builder().token("6558167523:AAEW-EF0a0an16sTOxuWUVppXMH-noewJZY").build()

    # Definir el manejador de conversación con las etapas y transiciones
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAIN_MENU: [
                CallbackQueryHandler(show_submenu, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(show_submenu, pattern="^" + str(TWO) + "$"),
                CallbackQueryHandler(show_submenu, pattern="^" + str(THREE) + "$"),
                CallbackQueryHandler(show_submenu, pattern="^" + str(FOUR) + "$"),
                CallbackQueryHandler(show_submenu, pattern="^" + str(FIVE) + "$"),
                CallbackQueryHandler(show_submenu, pattern="^" + str(SIX) + "$"),
                CallbackQueryHandler(show_submenu, pattern="^" + str(SEVEN) + "$"),
                CallbackQueryHandler(show_submenu, pattern="^" + str(EIGHT) + "$"),
            ],
            SUB_MENU: [
                CallbackQueryHandler(start_over, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(handle_submenu_choice, pattern="^(2|3|4|5|6|7|8)$"),
            ],
            END_ROUTES: [
                CallbackQueryHandler(start_over, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(end, pattern="^(2|3|4|5|6|7|8)$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    # Agregar el manejador de conversación a la aplicación
    application.add_handler(conv_handler)

    # Iniciar la aplicación y esperar actualizaciones
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    # Ejecutar la función principal si el script es ejecutado directamente
    main()

