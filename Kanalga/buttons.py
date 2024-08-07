from telebot import types

checkbtns = types.InlineKeyboardMarkup(row_width=1)
checkbtns.add(
    types.InlineKeyboardButton(text="➕Obuna bo'lish", url="https://t.me/campuzb"),
    types.InlineKeyboardButton(text="✅Tasdiqlash", callback_data="checksub")
)

# kannallar = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="➕Obuna bo'lish", url= 'https://t.me/manol1_gaplar')],
#         [InlineKeyboardButton(text="✅Tasdiqlash", callback_data='tastiqlash')]
#     ]
# )