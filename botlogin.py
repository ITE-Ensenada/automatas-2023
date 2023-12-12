import logging
import re
import pymysql.cursors
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)

TOKEN = "6632243325:AAFxL6Wbn1WLugHZR_1_tHHiWLMTaMdRfHY"
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="jorgealberto",  # jorgealberto
    password="Tecnologic0123!",  # Tecnologic0123!
    database="tronkos_itebot",  # tronkos_itebot
    cursorclass=pymysql.cursors.DictCursor,
)

COMMAND_EMAIL = "/correo"
CORREO = range(1)
CURPVERIFICATION = range(2)
pattern = r"^\S+@(ite\.edu\.mx|ensenada\.tecmn\.mx)$"
CURP = ""


# Debe de ser un boton START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Escribe tu correo en minusculas porfavor")
    return CORREO


async def correo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global CURP
    if re.match(pattern, update.message.text):
        messagetext: str = "Tu correo es: " + update.message.text.lower()
        await update.message.reply_text(messagetext)
        await context.bot.delete_message(
            chat_id=update.message.chat_id, message_id=update.message.message_id
        )
        # Validar si existe en la base de datos aqui
        with connection.cursor() as cursor:
            # fetchone
            sql_alumno = "SELECT `CURP` FROM `alumno` WHERE `Correo`=%s"
            cursor.execute(sql_alumno, (update.message.text.lower()))
            result = cursor.fetchone()
            if result:
                CURP = result["CURP"]
                print(CURP)

            else:
                # Si no hay resultados en la primera tabla buscar en la tabla maestros
                sql_docente = "SELECT `CURP` FROM `docente` WHERE `Correo`=%s"
                cursor.execute(sql_docente, (update.message.text.lower()))
                result = cursor.fetchone()
                if result:
                    CURP = result["CURP"]
                    print(CURP)
                else:
                    print("No se encontraron resultados para el correo proporcionado.")
    else:
        # Boton de CANCEL
        await update.message.reply_text(
            "Tu correo no es VALIDO (No cumple con las especificaciones del correo institucional del ite) Use: /cancel"
        )
    # print f // print in console
    print(
        f"Usted ({update.message.chat_id}): escribio: {messagetext} Tu id usuario es:{context._user_id}"
    )

    await update.message.reply_text("Escribe tu Curp")
    return CURPVERIFICATION


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    await update.message.reply_text(
        "Adios, si quiere reintentar, utilice /start",
        reply_markup=ReplyKeyboardRemove(),
    )

    return ConversationHandler.END


async def curpverification(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messagetext: str = "Tu curp es " + update.message.text.upper()
    await context.bot.delete_message(
        chat_id=update.message.chat_id, message_id=update.message.message_id
    )
    userID: str = context._user_id
    if update.message.text == CURP:
        await update.message.reply_text(
            "CURP VALIDO - Bienvenido : Tu numero de usuario es:"
        )
        await update.message.reply_text(userID)
    else:
        await update.message.reply_text(
            "El Curp no concuerda con la base de datos: use /cancel para salir o intente de nuevo"
        )
        return CURPVERIFICATION


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
        ],
        states={
            CORREO: [MessageHandler(filters.TEXT & (~filters.COMMAND), correo)],
            CURPVERIFICATION: [
                MessageHandler(filters.TEXT & (~filters.COMMAND), curpverification)
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    print("starting")
    main()
