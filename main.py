import logging
import os
from telegram.ext import ApplicationBuilder

# Konfigurasi Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Masukkan Token dari @BotFather di sini
TOKEN = "MASUKKAN_TOKEN_BOT_ANDA_DI_SINI"

def main():
    if TOKEN == "MASUKKAN_TOKEN_BOT_ANDA_DI_SINI":
        print("❌ Error: TOKEN belum diisi di main.py!")
        return

    # Inisialisasi Application
    application = ApplicationBuilder().token(TOKEN).build()
    
    print("🚀 Bot sedang berjalan...")
    application.run_polling()

if __name__ == '__main__':
    main()
