import logging
import random
import os
from telegram import ForceReply, Update, InputFile, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup  
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext, CallbackQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# List of Pokémon images and their names (you can add more)
pokemons = [
    {"name": "Pikachu", "image": "pikachu.jpg"},
    {"name": "Charizard", "image": "charizard.jpg"},
    {"name": "Squirtle", "image": "squirtle.jpg"},
    {"name": "Bulbasaur", "image": "bulbasaur.jpg"},
    {"name": "Charmander", "image": "charmander.jpg"},
]

# Dictionary to store user scores
user_scores = {}

# Dictionary to track whether the menu has been shown to a user
user_menu_shown = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    user_scores[user.id] = 0  # Initialize user's score

    # Show the menu if it hasn't been shown to the user before
    if not user_menu_shown.get(user.id):
        await show_menu(update)
        user_menu_shown[user.id] = True


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Guess the Pokémon's name from the image!")


async def show_menu(update: Update) -> None:
    """Show the menu with "Start" and "Help" buttons."""
    buttons = [[KeyboardButton("Start"), KeyboardButton("Help")]]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)

async def send_random_pokemon(bot, chat_id):
    """Send a random Pokémon image to the user and return the correct Pokémon name."""
    random_pokemon = random.choice(pokemons)
    image_path = os.path.join("pokemon_images", random_pokemon["image"])
    with open(image_path, "rb") as image_file:
        # Crea un teclado personalizado con cuatro opciones de respuesta
        keyboard = [
            [
                InlineKeyboardButton(random.choice(pokemons)["name"], callback_data='incorrect'),
                InlineKeyboardButton(random.choice(pokemons)["name"], callback_data='incorrect'),
            ],
            [
                InlineKeyboardButton(random.choice(pokemons)["name"], callback_data='incorrect'),
                InlineKeyboardButton(random_pokemon["name"], callback_data='correct'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await bot.send_photo(
            chat_id=chat_id,
            photo=InputFile(image_file),
            caption="Guess the Pokémon's name from the image!",
            reply_markup=reply_markup,
        )
    return random_pokemon["name"].lower()  # Devuelve el nombre del Pokémon en minúsculas


async def check_answer(update: Update, context: CallbackContext):
    user = update.effective_user
    message_text = update.message.text.strip().lower()

    if user.id not in user_scores:
        user_scores[user.id] = 0

    # Obtén el nombre correcto del Pokémon mostrado en la imagen
    correct_answer = context.user_data.get("correct_answer")

    if correct_answer:
        if message_text == correct_answer:
            user_scores[user.id] += 1
            await update.message.reply_text(f"Correct! You've earned 1 point. Your total score: {user_scores[user.id]}.")
        else:
            await update.message.reply_text("Incorrect! The correct answer is: " + correct_answer)

    # Envía la siguiente imagen y actualiza el nombre correcto
    correct_answer = await send_random_pokemon(context.bot, update.message.chat_id)
    context.user_data["correct_answer"] = correct_answer

# Agrega un manejador para procesar los botones de respuesta
async def handle_button(update: Update, context: CallbackContext):
    query = update.callback_query
    user = update.effective_user

    if query.data == 'correct':
        user_scores[user.id] += 1
        await query.message.reply_text(f"Correct! You've earned 1 point. Your total score: {user_scores[user.id]}.")
    elif query.data == 'incorrect':
        correct_answer = context.user_data.get("correct_answer")
        await query.message.reply_text("Incorrect! The correct answer is: " + correct_answer)
        
def main() -> None:
    """Start the bot."""
    application = Application.builder().token("6495306746:AAGHk08d4iZIOiOe2w3fLjz2SlHRFtF12o8").build()

    os.makedirs("pokemon_images", exist_ok=True)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

async def handle_menu_choice(update: Update, context: CallbackContext):
    user_choice = update.message.text

    if user_choice == "Start":
        await start(update, context)
    elif user_choice == "Help":
        await help_command(update, context)

if __name__ == "__main__":
    main()

