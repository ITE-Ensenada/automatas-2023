#!/usr/bin/env python
# pylint: disable=unused-argument


import os
from processing import (
    blur_image,
    greyscale,
    enhance_color,
    contour
)
from telegram import (
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove, 
    Update)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

API_KEY = os.getenv("TELEGRAM_BOT_KEY")
PHOTO, SET_MODE = range(2)
MODE = ''
filter_functions = {
    'blur': blur_image,
    'b/w': greyscale,
    'enhance': enhance_color ,
    'contour': contour
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation"""
    reply_keyboard = [
        ["Blur", "B/W", "Enhance"],
        ["Contour"]
        ]

    await update.message.reply_text(
        "Please select a filter and then send a photo",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Filter"
        ),
    )

    return SET_MODE


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    """Receives image, then applies filter"""

    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive("photo.jpg")
    await update.message.reply_text(
        "Here's your processed image:"
    )
    filter_functions[MODE]("photo.jpg")
    await update.message.reply_photo("photo.jpg")


async def set_mode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    global MODE
    MODE = update.message.text.lower()
    await update.message.reply_text(f"You selected {MODE}. Now send me the photo!")

    return PHOTO


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    application = Application.builder().token(API_KEY).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            PHOTO: [MessageHandler(filters.PHOTO, photo)],
            SET_MODE: [MessageHandler(filters.Regex(
                "^(Blur|Enhance|B/W|Contour)$"
                ), set_mode)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()