from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.set_menu import set_main_menu

router_set_menu = Router()


# Хэндлер удаляет по команде /delmenu кнопку 'menu'
@router_set_menu.message(Command('delmenu'))
async def process_delmenu_command(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка <b>"menu"</b> удалена')


# Хэндлер создает по комнаде /createmenu кнопку 'menu'
@router_set_menu.message(Command('createmenu'))
async def process_createmenu_command(message: Message, bot: Bot):
    await set_main_menu(bot)
    await message.answer(text='Кнопка <b>"menu"</b> создана')
