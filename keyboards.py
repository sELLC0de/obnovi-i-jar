from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("1. Merry Chef Новая"),
    KeyboardButton("2. Merry Chef Старая"),
)
main_menu.add(
    KeyboardButton("3. Copa"),
    KeyboardButton("4. Copa FIT")
)
main_menu.add(
    KeyboardButton("Я не знаю какая печь")
)

back_button = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("🔙 Назад в главное меню"))

sub_menu = InlineKeyboardMarkup(row_width=1)
sub_menu.add(
    InlineKeyboardButton("📘 Как скачать на флешку", callback_data="download_info"),
    InlineKeyboardButton("🆘 Получить помощь", url="https://t.me/rn_star"),
    InlineKeyboardButton("🔙 Назад в главное меню", callback_data="back_to_main")
)
