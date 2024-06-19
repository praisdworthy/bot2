from aiogram.types import  (
                           InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           ReplyKeyboardMarkup,
                           KeyboardButton)



menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='меню')],
        [KeyboardButton(text='голосование')]
    ]
)


anket_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='заполнить анкету')]
    ]
)


link_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='тгк', url='https://t.me/+MPFubbZ_99I1Yzc6')],
            [InlineKeyboardButton(text='тг альфа', url='https://t.me/AlfaBank')],
            [InlineKeyboardButton(text='сф', url='https://www.w3schools.com/python/ref_func_input.asp')],
        ]
    )


clothes_sell = ReplyKeyboardMarkup(
           keyboard=[
               [KeyboardButton(text='кроссовки')],
               [KeyboardButton(text='майки')],
               [KeyboardButton(text='кофты')],
               [KeyboardButton(text='голосование')]
           ]
       )


sneakers_sell = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='adidas', url='https://www.adidas.com/us')],
        [InlineKeyboardButton(text='nike', url='https://www.nike.com/ru/')],
        [InlineKeyboardButton(text='reebok', url='https://www.reebok.ru/')]
    ]
)


tshirt_sell = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='adidas', url='https://www.adidas.com/us')],
        [InlineKeyboardButton(text='nike', url='https://www.nike.com/ru/')],
        [InlineKeyboardButton(text='reebok', url='https://www.reebok.ru/')]
    ]
)


hudi_sell = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='adidas', url='https://www.adidas.com/us')],
        [InlineKeyboardButton(text='nike', url='https://www.nike.com/ru/')],
        [InlineKeyboardButton(text='reebok', url='https://www.reebok.ru/')]
    ]
)

