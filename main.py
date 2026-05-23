import logging
import os
import requests
import importlib
from telegram.ext import ApplicationBuilder, CommandHandler

# --- KONFIGURASI LOGGING ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- FUNGSI START ---
async def start(update, context):
    await update.message.reply_text("Sistem Bot Aktif! Gunakan /install <url_raw_github> untuk memasang skill baru.")

def main():
    # Mengambil token dari Railway Variables (Cara 2 yang Aman)
    TOKEN = os.getenv("BOT_TOKEN")
    
    if not TOKEN:
        print("ERROR: BOT_TOKEN tidak ditemukan di Environment Variables!")
        return

    # drop_pending_updates=True akan membuang konflik koneksi yang lama
    application = ApplicationBuilder().token(TOKEN).build()
    application.bot.delete_webhook(drop_pending_updates=True)

    # Handler Dasar
    application.add_handler(CommandHandler("start", start))

    # --- FUNGSI INSTALLER ---
    async def install_skill(update, context):
        if not context.args:
            await update.message.reply_text("Kirimkan URL raw GitHub untuk menginstal skill.")
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
                    await update.message.reply_text(f"Skill '{file_name}' berhasil diinstal!")
                else:
                    await update.message.reply_text("Skill berhasil diunduh, tapi tidak ada fungsi setup().")
            else:
                await update.message.reply_text("Gagal mengunduh file, periksa URL-nya.")
        except Exception as e:
            await update.message.reply_text(f"Error instalasi: {str(e)}")

    application.add_handler(CommandHandler("install", install_skill))

    print("Bot sedang berjalan...")
    application.run_polling()

if __name__ == '__main__':
    main()
