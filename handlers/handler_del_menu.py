"""Хэндлер удаляет по команде /delmenu кнопку 'menu' из бота"""

from aiogram import Router, Bot
from aiogram.types import Message

router_del = Router()


@router_del.message(lambda message: message.text == '/delmenu')
async def process_delmenu_command(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "menu" удалена')
