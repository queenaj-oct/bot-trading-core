import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8942976552:AAElLSGizgcCXsT66FBmoH1ga8_URTSiq_g"

# Fungsi untuk merespons /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot sudah bangun! Kirim link skill untuk memulai instalasi.")

# Fungsi untuk merespons pesan teks biasa (Echo)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Saya menerima pesan Anda: {update.message.text}")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Menambahkan handler agar bot bisa merespons
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    
    print("🚀 Bot sedang berjalan dan siap menjawab...")
    application.run_polling()

if __name__ == '__main__':
    main()
