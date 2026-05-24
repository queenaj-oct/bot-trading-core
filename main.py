import os
import logging
from telegram.ext import ApplicationBuilder

# --- KONFIGURASI LOGGING ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- TOKEN BOT ---
# Pastikan Anda sudah menyetel environment variable 'TOKEN' di dashboard worker Anda
TOKEN = os.getenv("TOKEN")

def main():
    if not TOKEN:
        print("❌ Error: Token bot tidak ditemukan di Environment Variables!")
        return

    # Inisialisasi Bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Jika Anda memiliki sistem plugin/skill otomatis, biarkan kosong di sini 
    # karena Anda akan menginstalnya via perintah /install nanti.
    
    print("🚀 Bot sedang berjalan...")
    application.run_polling()

if __name__ == '__main__':
    main()
