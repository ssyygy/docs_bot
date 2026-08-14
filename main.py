import asyncio
import os

from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, MessageHandler, filters, ContextTypes

app = Flask(__name__)

# Токен берем из переменных окружения (не храним в коде!)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TOKEN)


# Ваша логика обработки (здесь вы вставляете OCR)
async def handle_docs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ваш договор генерируется... (тут ваша магия)")


# Создаем приложение телеграма на уровне модуля,
# чтобы это выполнялось и при запуске через gunicorn (main:app),
# а не только при прямом запуске файла.
application = Application.builder().token(TOKEN).build()
application.add_handler(MessageHandler(filters.PHOTO, handle_docs))

# Отдельный event loop для обработки апдейтов внутри синхронного Flask
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(application.initialize())


# Эндпоинт для вебхука
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    loop.run_until_complete(application.process_update(update))
    return 'ok', 200


@app.route('/')
def index():
    return "Бот жив!", 200


# Устанавливаем вебхук один раз при импорте модуля
webhook_url = f'https://{os.environ.get("RENDER_EXTERNAL_HOSTNAME")}/{TOKEN}'
loop.run_until_complete(bot.set_webhook(url=webhook_url))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))