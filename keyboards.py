from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("1. Merry Chef Новая"),
    KeyboardButton("2. Merry Chef Старая"),
)
main_menu.add(
    KeyboardButton("3. Copa"),
    KeyboardButton("4. Copa Feed")
)

back_button = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("🔙 Назад в главное меню"))

sub_menu = ReplyKeyboardMarkup(resize_keyboard=True)
sub_menu.add(
    KeyboardButton("📘 Инструкция по обновлению"),
    KeyboardButton("📁 Файл для обновления")
)
sub_menu.add(KeyboardButton("🔙 Назад в главное меню"))
