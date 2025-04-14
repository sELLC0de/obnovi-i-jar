from aiogram import types, Dispatcher
from aiogram.types import InputFile, InputMediaPhoto, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
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
        await message.answer("Вы выбрали: Merry Chef Новая")
        await message.answer_photo(InputFile("images/merry_new_setting.jpg"), caption="Инструкция по обновлению")

        link_keyboard = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("📁 Файл для обновления", url="https://disk.yandex.ru/d/e2SUBFMC_vHNPQ")
        )
        link_keyboard.inline_keyboard += sub_menu.inline_keyboard  # добавляем кнопки из sub_menu

        await message.answer("Нажмите кнопку ниже, чтобы скачать файл:", reply_markup=link_keyboard)

    elif message.text.startswith("2. Merry Chef Старая"):
        await message.answer("Вы выбрали: Merry Chef Старая")
        await message.answer_photo(InputFile("images/merry_old_setting.jpg"), caption="Инструкция по обновлению")

        link_keyboard = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("📁 Файл для обновления", url="https://disk.yandex.ru/d/SgDZr_kvyLXmXA")
        )
        link_keyboard.inline_keyboard += sub_menu.inline_keyboard  # добавляем кнопки из sub_menu

        await message.answer("Нажмите кнопку ниже, чтобы скачать файл:", reply_markup=link_keyboard)

    elif message.text.startswith("3. Copa"):
        await message.answer("Вы выбрали: Copa")
        await message.answer_photo(InputFile("images/copa_setting.jpg"), caption="Инструкция по обновлению")

        link_keyboard = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("📁 Файл для обновления", url="https://disk.yandex.ru/d/mVUGuhpj6o1TkA")
        )
        link_keyboard.inline_keyboard += sub_menu.inline_keyboard  # добавляем кнопки из sub_menu

        await message.answer("Нажмите кнопку ниже, чтобы скачать файл:", reply_markup=link_keyboard)

    elif message.text.startswith("4. Copa FIT"):
        await message.answer("Вы выбрали: Copa FIT")
        await message.answer_photo(InputFile("images/copafitsetting.jpg"), caption="Инструкция по обновлению")

        link_keyboard = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("📁 Файл для обновления", url="https://disk.yandex.ru/d/VxRp_sjVTH-fjw")
        )
        link_keyboard.inline_keyboard += sub_menu.inline_keyboard  # добавляем кнопки из sub_menu

        await message.answer("Нажмите кнопку ниже, чтобы скачать файл:", reply_markup=link_keyboard)

    elif message.text == "Я не знаю какая печь":
        media_paths = [
            ("images/new_merrychef.jpg", "Это Новая Merry Chef"),
            ("images/old_merrychef.jpg", "Это Старая Merry Chef"),
            ("images/copa_fit.jpg", "Это Copa Fit"),
            ("images/copa.jpg", "Это Copa")
        ]

        for path, _ in media_paths:
            if not os.path.exists(path):
                await message.answer(f"Файл {path} не найден!")
                return

        await message.chat.do("upload_photo")

        media = [
            InputMediaPhoto(media=InputFile(path), caption=caption if idx == 0 else None)
            for idx, (path, caption) in enumerate(media_paths)
        ]

        try:
            await message.answer_media_group(media)
            await message.answer("Выберите подходящую печь или вернитесь в меню:", reply_markup=back_to_menu_keyboard)
        except Exception as e:
            await message.answer(f"Произошла ошибка при отправке медиа: {e}")

    elif message.text == "🔙 Назад в главное меню":
        await message.answer("Вы вернулись в главное меню. Выберите Вашу печку:", reply_markup=main_menu)

    else:
        await message.answer("Я не понял команду. Пожалуйста, выберите пункт из меню.")

# 🆕 Callback-кнопка: инструкция по флешке
async def send_flash_instruction(callback: types.CallbackQuery):
    await callback.answer()
    image_path = "images/orig.jpg"
    if os.path.exists(image_path):
        await callback.message.answer_photo(InputFile(image_path), caption="Вот как записать файл на флешку 💾")
    else:
        await callback.message.answer("Изображение не найдено!")

# 🆕 Callback-кнопка: назад в главное меню
async def back_to_main(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Вы вернулись в главное меню. Выберите Вашу печку:", reply_markup=main_menu)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start"])
    dp.register_message_handler(main_menu_handler)

    # 👇 Новые callback-обработчики
    dp.register_callback_query_handler(send_flash_instruction, Text(equals="download_info"))
    dp.register_callback_query_handler(back_to_main, Text(equals="back_to_main"))
