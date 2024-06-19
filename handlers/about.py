from aiogram.types import Message
from aiogram.filters import Command
from markup import link_keyboard
from aiogram import Router


router = Router()


@router.message(Command('about'))
async def about(message: Message):
    text = '[информация](https://t.me/+MPFubbZ_99I1Yzc6) `о боте`'
    await message.answer(text=text, reply_markup=link_keyboard, parse_mode='MarkdownV2')
    await message.delete()