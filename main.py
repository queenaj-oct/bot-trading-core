import logging
from telegram.ext import ApplicationBuilder

# --- KONFIGURASI LOGGING ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Masukkan Token Bot Anda di antara tanda kutip di bawah ini
TOKEN = "MASUKKAN_TOKEN_BOT_ANDA_DISINI"

def main():
    if TOKEN == "MASUKKAN_TOKEN_BOT_ANDA_DISINI":
        print("❌ Error: Silakan isi TOKEN di dalam file main.py!")
        return

    # Inisialisasi Bot
    application = ApplicationBuilder().token(TOKEN).build()
    
    print("🚀 Bot sedang berjalan...")
    application.run_polling()

if __name__ == '__main__':
    main()
