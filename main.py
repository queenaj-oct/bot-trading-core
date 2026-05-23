import os
import importlib
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")
SKILLS_DIR = "skills"

if not os.path.exists(SKILLS_DIR):
    os.makedirs(SKILLS_DIR)
    with open(f"{SKILLS_DIR}/__init__.py", "w") as f:
        f.write("")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sistem Bot Aktif! Gunakan /install <url_raw_github> untuk memasang skill baru.")

async def install_skill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Format: /install <url_raw_github_file.py>")
        return

    url = context.args[0]
    filename = url.split("/")[-1]

    if not filename.endswith(".py"):
        await update.message.reply_text("Gagal: File skill harus berformat .py")
        return

    await update.message.reply_text(f"Mengunduh skill {filename}...")

    try:
        response = requests.get(url)
        response.raise_for_status()

        filepath = os.path.join(SKILLS_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response.text)

        module_name = filename[:-3]
        importlib.invalidate_caches()
        module = importlib.import_module(f"{SKILLS_DIR}.{module_name}")

        if hasattr(module, 'setup'):
            module.setup(context.application)
            await update.message.reply_text(f"Skill '{filename}' berhasil diinstal dan diaktifkan!")
        else:
            await update.message.reply_text(f"Skill '{filename}' diunduh, tapi tidak valid (tidak ada fungsi setup).")

    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat mengunduh: {e}")

def main():
    if not TOKEN:
        print("Error: TELEGRAM_TOKEN belum disetting di Railway!")
        return

    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("install", install_skill))
    
    print("Bot sedang berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()

