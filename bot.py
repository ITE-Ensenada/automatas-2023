import logging
import random
import os
from telegram import Update, InputFile, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# List of Pokémon images and their names (you can add more)
pokemons = [
    {"name": "Bulbasaur", "image": "bulbasaur.jpg"},
    {"name": "Ivysaur", "image": "ivysaur.jpg"},
    {"name": "Venusaur", "image": "venusaur.jpg"},
    {"name": "Charmander", "image": "charmander.jpg"},
    {"name": "Charmeleon", "image": "charmeleon.jpg"},
    {"name": "Charizard", "image": "charizard.jpg"},
    {"name": "Squirtle", "image": "squirtle.jpg"},
    {"name": "Wartortle", "image": "wartortle.jpg"},
    {"name": "Blastoise", "image": "blastoise.jpg"},
    {"name": "Pikachu", "image": "pikachu.jpg"},
]

# Dictionary to store user scores
user_scores = {}
# Dictionary to keep track of shown Pokémon
shown_pokemons = {}

async def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    user_scores[user.id] = {"score": 0, "total_pokemons": 0}  # Initialize user's score and total Pokémon count
    await send_random_pokemon(update.message.chat_id, context.bot, user.id, context)

async def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Guess the Pokémon's name from the image!")

async def send_random_pokemon(chat_id, bot, user_id, context):
    """Send a random Pokémon image to the user and return the correct Pokémon name."""
    # Generate a list of Pokémon not shown to the user
    available_pokemons = [pokemon for pokemon in pokemons if pokemon["name"].lower() not in shown_pokemons.get(user_id, [])]
    
    if not available_pokemons:
        await end_game(chat_id, user_id, context.bot, context)
        return
    
    random_pokemon = random.choice(available_pokemons)
    shown_pokemons.setdefault(user_id, []).append(random_pokemon["name"].lower())
    
    # Shuffle the options including the correct answer
    options = [random_pokemon["name"]]
    while len(options) < 4:
        random_option = random.choice(pokemons)["name"]
        if random_option not in options:
            options.append(random_option)
    
    random.shuffle(options)
    
    image_path = os.path.join("pokemon_images", random_pokemon["image"])
    with open(image_path, "rb") as image_file:
        keyboard = ReplyKeyboardMarkup(
            [[KeyboardButton(option)] for option in options], one_time_keyboard=True
        )
        await bot.send_photo(
            chat_id=chat_id,
            photo=InputFile(image_file),
            caption="Guess the Pokémon's name from the image!",
            reply_markup=keyboard,
        )
    return random_pokemon["name"].lower()  # Devuelve el nombre del Pokémon en minúsculas

async def check_answer(update: Update, context: CallbackContext):
    user = update.effective_user
    message_text = update.message.text.strip().lower()

    if user.id not in user_scores:
        user_scores[user.id] = {"score": 0, "total_pokemons": 0}

    # Obtén el nombre correcto del Pokémon mostrado en la imagen
    correct_answer = context.user_data.get("correct_answer")

    if correct_answer:
        if message_text == correct_answer:
            user_scores[user.id]["score"] += 1
            await update.message.reply_text(f"Correct! You've earned 1 point. Your total score: {user_scores[user.id]['score']}.")

    # Actualiza el total de Pokémon mostrados al usuario
    user_scores[user.id]["total_pokemons"] += 1

    # Envía la siguiente imagen y actualiza el nombre correcto
    correct_answer = await send_random_pokemon(update.message.chat_id, context.bot, user.id, context)
    context.user_data["correct_answer"] = correct_answer

async def end_game(chat_id, user_id, bot, context):
    user_score = user_scores[user_id]["score"]
    total_pokemons = user_scores[user_id]["total_pokemons"]
    await bot.send_message(chat_id, f"Game Over! Your score: {user_score} correct answers out of {total_pokemons} Pokémon.")
    # Eliminar el estado del juego del usuario al finalizar
    del user_scores[user_id]
    del shown_pokemons[user_id]

async def handle_menu_choice(update: Update, context: CallbackContext):
    user_choice = update.message.text

    if user_choice == "Start":
        await start(update, context)
    elif user_choice == "Help":
        await help_command(update, context)


def main() -> None:
    """Start the bot."""
    application = Application.builder().token("6495306746:AAGHk08d4iZIOiOe2w3fLjz2SlHRFtF12o8").build()

    os.makedirs("pokemon_images", exist_ok=True)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()