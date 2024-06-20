from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from states import Form
from re import fullmatch
from markup import menu_button
from database import create_profile, edit_profile
from states import Menu


router = Router()


@router.message(Form.wait)
async def waititng(message: Message, state: FSMContext):
    await state.update_data(id=message.from_user.id)
    if message.text.lower() == 'заполнить анкету':
        await state.set_state(Form.name)
        text='введите имя'
        await message.answer(text=text)
    else:
        text='я тебя не понимаю( нажми на кнопку ниже, чтобы начачть заполнять анкету'
        await message.answer(text=text)


@router.message(Form.name)
async def name(message: Message, state: FSMContext):
    if message.text.isalpha():
        await state.update_data(name=message.text)
        await state.set_state(Form.age)
        text = ('введите возвраст')
        await message.answer(text=text)
    else:
        text = 'введите корректное имя'
        await message.answer(text=text)


@router.message(Form.age)
async def age(message: Message, state: FSMContext):
    if message.text.isdigit():
        if int(message.text) < 18:
            text = 'для вас функция недоступна'
            await message.answer(text=text)
            await state.set_state(Form.stop)
        else:
            await state.set_state(Form.email)
            await state.update_data(age=message.text)
            text = ('введите email')
            await message.answer(text=text)
    else:
       text = 'я вас не понимаю, используйте цифры'
       await message.answer(text=text)


@router.message(Form.stop)
async def age(message: Message, state: FSMContext):
    pass


@router.message(Form.email)
async def email(message: Message, state: FSMContext):
    if fullmatch('([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+)', message.text):
        await state.update_data(email=message.text)
        data_dict = await state.get_data()
        await create_profile(data_dict['id'])
        await edit_profile(data_dict['id'],(data_dict['name']),(data_dict['age']),(data_dict['email']))
        await message.answer('анкета заполнена, нажми на кнопку ниже чтобы открыть меню \n Также можете пройти голосование',
                             reply_markup=menu_button
                             )
        await state.set_state(Menu.menu)
    else:
        text = 'введите корректное email'
        await message.answer(text=text)







