from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

app = Flask(__name__)

# Токен берем из переменных окружения (не храним в коде!)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TOKEN)

# Ваша логика обработки (здесь вы вставляете OCR)
async def handle_docs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ваш договор генерируется... (тут ваша магия)")

# Эндпоинт для вебхука
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    # Запускаем асинхронную функцию
    application.process_update(update)
    return 'ok', 200

@app.route('/')
def index():
    return "Бот жив!", 200

if __name__ == '__main__':
    # Создаем приложение телеграма
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.PHOTO, handle_docs))
    
    # Устанавливаем вебхук (один раз при старте)
    bot.set_webhook(url=f'https://{os.environ.get("RENDER_EXTERNAL_HOSTNAME")}/{TOKEN}')
    
    # Запускаем Flask
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))