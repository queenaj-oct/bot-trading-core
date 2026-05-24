import logging
from telegram.ext import ApplicationBuilder

# Logging agar Anda bisa melihat proses di dashboard worker
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# GANTI DENGAN TOKEN ANDA
TOKEN = "ISI_TOKEN_BOT_DISINI"

def main():
    if TOKEN == "8942976552:AAElLSGizgcCXsT66FBmoH1ga8_URTSiq_g":
        print("❌ Error: TOKEN belum diisi di main.py!")
        return

    application = ApplicationBuilder().token(TOKEN).build()
    
    print("🚀 Bot sedang berjalan...")
    application.run_polling()

if __name__ == '__main__':
    main()
