import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os

# Configurar o logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Função de início do bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Olá! Eu sou o CFN4FaucetBot. Você pode obter tokens CFN4 aqui!")

# Função para processar comandos
async def faucet(update: Update, context: CallbackContext) -> None:
    # Aqui você pode adicionar a lógica para distribuir os tokens, como verificar o saldo ou realizar a transferência
    await update.message.reply_text("Você recebeu seus tokens CFN4!")

# Função principal que inicializa o bot
async def main() -> None:
    # Obter o token do bot das variáveis de ambiente
    token = os.getenv("BOT_TOKEN")
    
    # Verificar se o token foi obtido com sucesso
    if token is None:
        logger.error("BOT_TOKEN não foi encontrado!")
        return
    
    # Criar a aplicação e passar o token
    application = Application.builder().token(token).build()

    # Adicionar os manipuladores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("faucet", faucet))

    # Iniciar o bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    # Não use asyncio.run(), apenas chame diretamente o método assíncrono
    asyncio.ensure_future(main())
    # Manter o loop de eventos aberto
    asyncio.get_event_loop().run_forever()
