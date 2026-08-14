from telegram import Update
from telegram.ext import Application, MessageHandler, filters

async def handle_photo(update: Update, context):
    # Скачиваем фото
    photo_file = await update.message.photo[-1].get_file()
    file_path = f"passport_{update.effective_user.id}.jpg"
    await photo_file.download_to_drive(file_path)
    
    # Отправляем в OCR
    text = extract_passport_data(file_path)
    
    # Отдаем AI для заполнения шаблона
    contract = fill_contract_with_ai(text)
    
    # Отправляем пользователю .docx или .pdf
    await update.message.reply_document(document=open(contract, 'rb'))