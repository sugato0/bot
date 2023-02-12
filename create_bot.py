import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = "6006850926:AAFWPA8H4zZAgqxmiRopQBnF7TwEQgn_dJ8"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
storage=MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot,
                storage=storage)