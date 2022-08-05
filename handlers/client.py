from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import bot
from parser import anime


async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply("какое сообщение хочешь закрепить? ответь на него")


# @dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Приветствую вас {message.from_user.full_name}!')


# @dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, f'Не беспокоить, разберетесь сами {message.from_user.full_name}!')


# @dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("следующий вопрос", callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Кто является вторым наследником колоссального титана?'
    answers = ['Бертольд', 'Армин', 'Эрвин Смит', 'Эрен ЙЕГЕР']
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Прежде чем унаследовать, он был горелой булочкой',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,

    )


# @dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('media/котя.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)



async def parser_news(message: types.Message):
    data = anime.parser()
    for item in data:
       await bot.send_message(message.from_user.id, f"{item['title']}\n\n"
                                                    f"{item['date']}\n"
                                                    f"{item['link']}\n\n"
                                                    f"{item['photo']}")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix=['!'])
    dp.register_message_handler(parser_news, commands=['news'])
