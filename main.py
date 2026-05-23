import logging
import os
import requests
import importlib
from telegram.ext import ApplicationBuilder, CommandHandler

# --- KONFIGURASI LOGGING ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update, context):
    await update.message.reply_text("Bot aktif! Gunakan /install <url_raw_github> untuk memasang skill.")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        print("ERROR: BOT_TOKEN tidak ditemukan!")
        return

    # Membangun aplikasi
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    # --- FUNGSI INSTALLER ---
    async def install_skill(update, context):
        if not context.args:
            await update.message.reply_text("Masukkan URL raw GitHub.")
            return
        
        url = context.args[0]
        try:
            response = requests.get(url)
            if response.status_code == 200:
                file_name = url.split('/')[-1]
                with open(file_name, 'w') as f:
                    f.write(response.text)
                
                module_name = file_name.replace('.py', '')
                module = importlib.import_module(module_name)
                
                if hasattr(module, 'setup'):
                    module.setup(application)
                    await update.message.reply_text(f"Skill '{file_name}' berhasil!")
                else:
                    await update.message.reply_text("Tidak ada fungsi setup().")
        except Exception as e:
            await update.message.reply_text(f"Error: {str(e)}")

    application.add_handler(CommandHandler("install", install_skill))

    print("Bot sedang berjalan...")
    # Polling yang benar di sini:
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
