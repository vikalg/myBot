import logging
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '5941486404:AAFgo_1GTKB0alvso5igTZQ4KBI2eRJ-SsY'

logging.basicConfig(level=API_TOKEN)

bot = Bot(token=API_TOKEN)
#Диспетчер
dp = Dispatcher(bot)
#/start
@dp.message_handler(commands=["start"]) #/start
async def cmd_start(message:types.Message):
    await message.answer("Hello!")

@dp.message_handler(commands=["help"])
async def help(message:types.Message):
    await message.answer("""/start - Начало работы
    /help - Получение справки
     /send - Прислать эмоджи животного при команде / send [животное]
      / dice - Игра""")

@dp.message_handler(commands="send")
async def send_animal(message: types.Message):
    animals_emojis = {"cat": "😺 ", "dog": "🐶", "unicorn": "🦄"}
    args = message.get_args()
    await message.answer(animals_emojis.get(args, f"Нет такого аргумента! Выбор : {', '.join(animals_emojis.keys())}"))

@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
