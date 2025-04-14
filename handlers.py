from aiogram import types, Dispatcher
from aiogram.types import InputFile, InputMediaPhoto, ReplyKeyboardMarkup, KeyboardButton
from keyboards import main_menu, sub_menu, back_button
import os

# Клавиатура с кнопкой "Назад"
back_to_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔙 Назад в главное меню")]
    ],
    resize_keyboard=True
)

async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Я бот-помощник по обновлению печей проекта \"Сгоряча\"\n\nВыберите Вашу печку:",
        reply_markup=main_menu
    )

async def main_menu_handler(message: types.Message):
    if message.text.startswith("1. Merry Chef Новая"):
        await message.answer("Вы выбрали: Merry Chef Новая", reply_markup=sub_menu)
        await message.answer_photo(InputFile("images/merry_new_setting.jpg"), caption="Инструкция по обновлению")
        await message.answer_document(InputFile("files/merry_new_update.zip"), caption="Файл для обновления")

    elif message.text.startswith("2. Merry Chef Старая"):
        await message.answer("Вы выбрали: Merry Chef Старая", reply_markup=sub_menu)
        await message.answer_photo(InputFile("images/merry_old_setting.jpg"), caption="Инструкция по обновлению")
        await message.answer_document(InputFile("files/merry_old_update.zip"), caption="Файл для обновления")

    elif message.text.startswith("3. Copa"):
        await message.answer("Вы выбрали: Copa", reply_markup=sub_menu)
        await message.answer_photo(InputFile("images/copa_setting.jpg"), caption="Инструкция по обновлению")
        await message.answer_document(InputFile("files/copa_old_update.zip"), caption="Файл для обновления")

    elif message.text.startswith("4. Copa FIT"):
        await message.answer("Вы выбрали: Copa FIT", reply_markup=sub_menu)
        await message.answer_photo(InputFile("images/copafitsetting.jpg"), caption="Инструкция по обновлению")
        await message.answer_document(InputFile("files/copa_fit_update.zip"), caption="Файл для обновления")

    elif message.text == "Я не знаю какая печь":
        media_paths = [
            ("images/new_merrychef.jpg", "Это Новая Merry Chef"),
            ("images/old_merrychef.jpg", "Это Старая Merry Chef"),
            ("images/copa_fit.jpg", "Это Copa Fit"),
            ("images/copa.jpg", "Это Copa")
        ]

        # Проверка и отправка каждого изображения по отдельности
        for path, caption in media_paths:
            if not os.path.exists(path):
                await message.answer(f"Файл {path} не найден!")
                return

            await message.chat.do("upload_photo")  # Анимация загрузки
            await message.answer_photo(InputFile(path), caption=caption)

        await message.answer("Выберите подходящую печь или вернитесь в меню:", reply_markup=back_to_menu_keyboard)

    elif message.text == "🔙 Назад в главное меню":
        await message.answer("Вы вернулись в главное меню. Выберите Вашу печку:", reply_markup=main_menu)

    else:
        await message.answer("Я не понял команду. Пожалуйста, выберите пункт из меню.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start"])
    dp.register_message_handler(main_menu_handler)
