from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
import random

tb = "bot_tokeni_shu_yerga_yozing"

bot = Bot(token=tb)
dp = Dispatcher()

@dp. message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Do'stim sen bot yaratishni uddalading.")


@dp. message(Command("rasm"))
async def rasm_handler(message:Message):
    random_num = random.randint(1, 10000)
    url = f"https://picsum.photos/400/300?random={random_num}"
    await message.answer_photo(photo=url, caption="Mana tasodifiy rasm")

@dp. message()
async def echo(message:Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())