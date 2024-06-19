from aiogram.types import Message
from aiogram import Router
from markup import clothes_sell
from states import Menu
from markup import sneakers_sell
from markup import tshirt_sell
from markup import hudi_sell



router = Router()
data = []

@router.message(Menu.menu)
async def reply(message: Message):
    if message.text.lower() in ['меню', '/menu']:
       text = '<b><i>меню</i></b>:\n\n кроссовки \n\n майки \n\n кофты'
       await message.answer(text=text, reply_markup=clothes_sell, parse_mode='HTML')
    elif message.text.lower()  == 'кроссовки':
        await message.answer(text='выбери в панели компанию кроссово', reply_markup=sneakers_sell)
    elif message.text.lower()  == 'майки':
        await message.answer(text='выбери в панели компанию', reply_markup=tshirt_sell)
    elif message.text.lower()  == 'кофты':
        await message.answer(text='выбери в панели компанию', reply_markup=hudi_sell)
    elif message.text.lower() == 'заполнить анкету':
        await message.answer(text='введите имя и фамилию')
    elif message.text.lower() == 'голосование':
        question = 'как бот?'
        options = ['круто','не круто']
        await message.answer_poll(question=question, options=options, is_anonymous=False, allows_multiple_answers=True)
    else:
        text = 'я тебя не понимаю'
        await message.answer(text=text)





