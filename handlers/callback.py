from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import bot


# @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("следующий вопрос", callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'Акито был все таки женщиной или мужчиной?'
    answers = ['Женщиной', 'Мужчиной', 'и то и другое']
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Акито была женщиной',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,

    )


async def quiz_3(call: types.CallbackQuery):
    # markup = InlineKeyboardMarkup()
    # button_call_2 = InlineKeyboardButton("следующий вопрос", callback_data='button_call_2')
    # markup.add(button_call_2)

    question = '2+2?'
    answers = ['4', '5', '98764']
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='иди в 1 класс',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        # reply_markup=markup,

    )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')
