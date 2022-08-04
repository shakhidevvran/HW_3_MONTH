from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import bot_db

from config import bot, ADMIN


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    info = State()
    price = State()


async def fsm_photo(message: types.Message):
    if message.chat.type == "private":
        if message.from_user.id in ADMIN:
            await FSMAdmin.photo.set()
            await message.answer(
                f'Приветствую вас {message.from_user.full_name} отправьте фото блюда, которое хотите добавить.')
        else:
            await message.answer('Ты не админ дурень')
    else:
        await message.reply('бот работает только в личных сообщениях.')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.answer('Напишите название блюда')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await FSMAdmin.next()
        await message.answer('Добавьте описание к нему')


async def load_info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info'] = message.text
        await FSMAdmin.next()
        await message.answer('Укажите цену блюда')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
        await bot.send_photo(message.from_user.id, data['photo'])
        await bot.send_message(message.from_user.id,
                               f"Name: {data['name']}\n"
                               f"Info: {data['info']}\n"
                               f"Price: {data['price']}")
    await bot_db.sql_command_insert(state)
    await state.finish()
    await message.answer('Спасибо!')


def register_handlers_fsm_bluda(dp: Dispatcher):
    dp.register_message_handler(fsm_photo, commands=['bludo'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types='photo')
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_info, state=FSMAdmin.info)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
