from telebot import TeleBot, types

import buttons

token = "7429906412:AAHfxo2FO2COctHhLRD1e0nmglxxvwFiens"
bot = TeleBot(token)


channel = "@campuzb"

@bot.message_handler(commands=["start"])
def start(msg: types.Message):
    checkuser = bot.get_chat_member(channel, msg.from_user.id).status
    if checkuser == "member" or checkuser == "admin" or checkuser== "creator":
        bot.send_message(msg.from_user.id ,"Obunanggiz tasdiqlandi✅ \n  Ijod namunanggizni quyidagi telegram akauntiga yuboring 🔽 \n t.me/Oromgohlar2024")
    else:
        bot.send_message(msg.from_user.id, "Assalomu Alaykum! \n 🏕️Botimizdan to’liq foydalanishingiz uchun quydagi kanalimizga obuna bo’ling❗️", reply_markup=buttons.checkbtns)

@bot.callback_query_handler(func=lambda x: x.data)
def query(msg: types.CallbackQuery):
    bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message.id)

    match msg.data:
        case "checksub":
                checkuser = bot.get_chat_member(channel, msg.from_user.id).status
    if checkuser == "member" or checkuser == "admin" or checkuser== "creator":
        bot.send_message(msg.from_user.id ,"Obunanggiz tasdiqlandi✅ \n Ijod namunanggizni quyidagi telegram akauntiga yuboring 🔽 \n t.me/Oromgohlar2024")
    else:
        bot.send_message(msg.from_user.id, "🏕️Botimizdan to’liq foydalanishingiz uchun quydagi kanalimizga obuna bo’ling❗️", reply_markup=buttons.checkbtns)



bot.polling()
