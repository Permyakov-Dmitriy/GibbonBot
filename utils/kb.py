from telebot import types


def keyboard(buttons):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for i in buttons:
        markup.add(types.KeyboardButton(i))

    return markup