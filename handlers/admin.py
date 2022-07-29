
# from aiogram import types, Dispatcher
# from config import bot, ADMIN
# import random
#
#
# async def game(message: types.Message):
#     if message.text.startswith('game'):
#         if message.chat.type != 'private':
#             if message.from_user.id == ADMIN:
#                 emg = ['🎯', '🎳', '🎲', '⚽', '🏀']
#                 r_emg = random.choice(emg)
#                 await bot.send_dice(message.chat.id, emoji=r_emg)
#             else:
#                 await message.answer('Ты не админ дурень')
#
#         else:
#             await message.answer('Это работает только в чатах')
#
#
# def register_handlers_admin(dp: Dispatcher):
#     dp.register_message_handler(game, commands=['game'])
