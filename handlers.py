from aiogram import Dispatcher, types
from aiogram.types import InputFile
from keyboards import main_menu, sub_menu, back_button

@dp.message_handler(commands=['start'])
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
        media = types.MediaGroup()
        media.attach_photo(InputFile('images/new_merrychef.jpg'), caption="Это Новая Merry Chef")
        media.attach_photo(InputFile('images/old_merrychef.jpg'), caption="Это Старая Merry Chef")
        media.attach_photo(InputFile('images/new_copa_fit.jpg'), caption="Это Новая Copa Fit")
        media.attach_photo(InputFile('images/old_copa_fit.jpg'), caption="Это Старая Copa Fit")
        await message.answer_media_group(media)

    elif message.text == "🔙 Назад в главное меню":
        await message.answer("Вы вернулись в главное меню. Выберите Вашу печку:", reply_markup=main_menu)

    else:
        await message.answer("Я не понял команду. Пожалуйста, выберите пункт из меню.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start"])
    dp.register_message_handler(main_menu_handler)
