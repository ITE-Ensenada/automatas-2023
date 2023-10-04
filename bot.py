import logging
import random
import os
import asyncio
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
# Timeout duration in seconds
TIMEOUT_DURATION = 10

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
    while len(options) < 3:  # Change this line to 3 options
        random_option = random.choice(pokemons)["name"]
        if random_option not in options:
            options.append(random_option)

    random.shuffle(options)

    image_path = os.path.join("pokemon_images", random_pokemon["image"])
    with open(image_path, "rb") as image_file:
        # Add the timer to the caption
        caption = f"Time left: {TIMEOUT_DURATION} seconds\nGuess the Pokémon's name from the image!"
        keyboard = ReplyKeyboardMarkup(
            [[KeyboardButton(option)] for option in options], one_time_keyboard=True
        )
        await bot.send_photo(
            chat_id=chat_id,
            photo=InputFile(image_file),
            caption=caption,
            reply_markup=keyboard,
        )

    # Start the timer
    context.user_data["timer_task"] = asyncio.create_task(timer_callback(chat_id, user_id, bot, context))

    return random_pokemon["name"].lower()  # Return the lowercase Pokémon name

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

        else:
            await update.message.reply_text(f"Incorrect! The correct answer is: {correct_answer.capitalize()}.")

    # Actualiza el total de Pokémon mostrados al usuario
    user_scores[user.id]["total_pokemons"] += 1

    # Cancelar el temporizador
    timer_task = context.user_data.get("timer_task")
    if timer_task:
        timer_task.cancel()

    # Envía la siguiente imagen y actualiza el nombre correcto
    correct_answer = await send_random_pokemon(update.message.chat_id, context.bot, user.id, context)
    context.user_data["correct_answer"] = correct_answer

async def timer_callback(chat_id, user_id, bot, context):
    await asyncio.sleep(TIMEOUT_DURATION)
    if user_id in shown_pokemons:
        shown_pokemons[user_id].pop()  # Eliminar el Pokémon actual para que no cuente como respondido
    await bot.send_message(chat_id, "Time's up! You didn't answer in time. The correct answer was not counted.")
    # Envía la siguiente imagen y actualiza el nombre correcto
    correct_answer = await send_random_pokemon(chat_id, bot, user_id, context)
    context.user_data["correct_answer"] = correct_answer

async def end_game(chat_id, user_id, bot, context):
    user_score = user_scores[user_id]["score"]
    total_pokemons = user_scores[user_id]["total_pokemons"]
    await bot.send_message(chat_id, f"Game Over! Your score: {user_score} correct answers out of {total_pokemons} Pokémon.")
    # Eliminar el estado del juego del usuario al finalizar
    del user_scores[user_id]
    del shown_pokemons[user_id]

async def rules(update: Update, context: CallbackContext):
    """Provide rules for the game."""
    rules_text = (
        "Game Rules:\n"
        "1. You will be shown an image of a Pokémon.\n"
        "2. You have a limited time to guess the Pokémon's name.\n"
        "3. You can provide your answer in text.\n"
        "4. The bot will verify your answer and provide feedback.\n"
        "5. You earn points for correct answers.\n"
        "6. You can check your current score at any time."
    )
    await update.message.reply_text(rules_text)

async def pokedex(update: Update, context: CallbackContext):
    """List the available Pokémon names."""
    pokemon_names = [pokemon["name"] for pokemon in pokemons]
    pokemon_list_text = "Available Pokémon:\n" + "\n".join(pokemon_names)
    await update.message.reply_text(pokemon_list_text)

def main() -> None:
    """Start the bot."""
    application = Application.builder().token("6495306746:AAGHk08d4iZIOiOe2w3fLjz2SlHRFtF12o8").build()

    os.makedirs("pokemon_images", exist_ok=True)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("rules", rules))
    application.add_handler(CommandHandler("pokedex", pokedex))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()