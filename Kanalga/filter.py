from typing import Any
from aiogram.filters import Filter
from config import Kanal_id
from aiogram import Bot
from aiogram.types import Message
from buttons import kannallar


# class M_Obuna(Filter):
#     async def __call__(self, message: Message, bot: Bot):
#         user_status = await  bot.get_chat_member(Kanal_id,  message.from_user.id)
#         if user_status.status in ['creator', 'andministrator', 'member']:
#                 return False
#         return True

class  M_Obuna(Filter):
    async def __call__(self, message: Message, bot: Bot):
        for i in Kanal_id:
            user_status = await bot.get_chat_member(i, message.from_user.id)
            if user_status.status in ['creator', 'administrator', "member"]:
                return True
            else:
                await bot.send_message(chat_id=message.from_user.id,text='❌ Kechirasiz botimizdan foydalanishdan oldin ushbu kanallarga a\'zo bo\'lishingiz kerak.',reply_markup=kannallar.as_markup())
