import logging
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
    # GANTI 'YOUR_TOKEN_HERE' dengan Token Bot Anda
    # Atau gunakan os.getenv("BOT_TOKEN") jika Anda menyimpannya di Railway Variables
    TOKEN = "YOUR_TOKEN_HERE" 

    # drop_pending_updates=True akan membuang konflik koneksi yang lama
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Menghapus webhook/antrean lama saat bot mulai
    application.bot.delete_webhook(drop_pending_updates=True)

    # Handler Dasar
    application.add_handler(CommandHandler("start", start))

    # --- PENGATURAN INSTALLER (Agar Anda bisa install skill dari GitHub) ---
    async def install_skill(update, context):
        if not context.args:
            await update.message.reply_text("Kirimkan URL raw GitHub untuk menginstal skill.")
            return
        
        url = context.args[0]
        # Logika instalasi sederhana (mengunduh file)
        import requests
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Menulis file ke server agar bisa di-import
                file_name = url.split('/')[-1]
                with open(file_name, 'w') as f:
                    f.write(response.text)
                
                # Mengimpor modul secara dinamis
                import importlib
                module_name = file_name.replace('.py', '')
                module = importlib.import_module(module_name)
                
                if hasattr(module, 'setup'):
                    module.setup(application)
                    await update.message.reply_text(f"Skill '{file_name}' berhasil diinstal dan diaktifkan!")
                else:
                    await update.message.reply_text("File berhasil diunduh, tapi tidak ada fungsi setup().")
            else:
                await update.message.reply_text("Gagal mengunduh file, periksa URL-nya.")
        except Exception as e:
            await update.message.reply_text(f"Error instalasi: {str(e)}")

    application.add_handler(CommandHandler("install", install_skill))

    print("Bot sedang berjalan...")
    application.run_polling()

if __name__ == '__main__':
    main()
