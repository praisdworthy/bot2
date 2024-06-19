from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    wait = State()
    name = State()
    age = State()
    email = State()
    stop = State()


class Menu(StatesGroup):
    to_menu = State()
    menu = State()


