from telegram.ext import ApplicationBuilder, CommandHandler
import os

async def start(update, context):
    await update.message.reply_text("Olá! Bem-vindo ao faucet CFN4! Envie seu endereço da rede Polygon para receber tokens CFN4.")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Erro: BOT_TOKEN não está definido.")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
