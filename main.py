import logging
import os
from telegram.ext import ApplicationBuilder, CommandHandler

# --- KONFIGURASI LOGGING ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update, context):
    await update.message.reply_text("Bot aktif dengan Webhook!")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    PORT = int(os.environ.get("PORT", 8080)) # Railway memberikan port otomatis
    URL = os.environ.get("PUBLIC_URL") # Anda harus set ini di Railway Variables

    if not TOKEN or not URL:
        print("ERROR: BOT_TOKEN atau PUBLIC_URL belum diset di Railway Variables!")
        return

    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    # Menjalankan Webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{URL}/{TOKEN}"
    )

if __name__ == '__main__':
    main()
