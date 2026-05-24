import logging
from telegram.ext import ApplicationBuilder

# Konfigurasi Logging agar muncul di dashboard worker
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# TOKEN ANDA SUDAH DIMASUKKAN DI SINI
TOKEN = "8942976552:AAElLSGizgcCXsT66FBmoH1ga8_URTSiq_g"

def main():
    if not TOKEN or ":" not in TOKEN:
        print("❌ ERROR: Format Token tidak valid!")
        return

    try:
        # Inisialisasi Application
        application = ApplicationBuilder().token(TOKEN).build()
        
        print("🚀 Menghubungkan ke Telegram...")
        print("✅ Bot Aktif dan Menunggu Perintah.")
        application.run_polling()
    except Exception as e:
        print(f"❌ Gagal menjalankan bot: {e}")

if __name__ == '__main__':
    main()
