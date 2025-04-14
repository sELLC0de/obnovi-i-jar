from aiogram import Dispatcher, types
from aiogram.types import InputFile
from keyboards import main_menu, sub_menu, back_button

async def start(message: types.Message):
    await message.answer("Выберите Вашу печку:", reply_markup=main_menu)

async def main_menu_handler(message: types.Message):
    if message.text.startswith("1. Merry Chef Новая"):
        await message.answer("Вы выбрали: Merry Chef Новая", reply_markup=sub_menu)
    elif message.text.startswith("2. Merry Chef Старая"):
        await message.answer("Вы выбрали: Merry Chef Старая", reply_markup=sub_menu)
    elif message.text.startswith("3. Copa"):
        await message.answer("Вы выбрали: Copa", reply_markup=sub_menu)
    elif message.text.startswith("4. Copa Feed"):
        await message.answer("Вы выбрали: Copa Feed", reply_markup=sub_menu)
    elif message.text == "🔙 Назад в главное меню":
        await message.answer("Вы вернулись в главное меню. Выберите Вашу печку:", reply_markup=main_menu)
    elif message.text == "📘 Инструкция по обновлению":
        # Пример: отправка изображения
        photo = InputFile("photos/merry_new.jpg")  # <-- путь к нужному файлу
        await message.answer_photo(photo, caption="Инструкция по обновлению")
    elif message.text == "📁 Файл для обновления":
        update_file = InputFile("files/merry_new_update.zip")  # <-- путь к нужному файлу
        await message.answer_document(update_file, caption="Вот файл для обновления.")
    else:
        await message.answer("Я не понял команду. Пожалуйста, выберите пункт из меню.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(main_menu_handler)
