import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# Configurar o logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Função de início do bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Olá! Eu sou o CFN4FaucetBot. Você pode obter tokens CFN4 aqui!")

# Função para processar comandos
def faucet(update: Update, context: CallbackContext) -> None:
    # Aqui você pode adicionar a lógica para distribuir os tokens, como verificar o saldo ou realizar a transferência
    update.message.reply_text("Você recebeu seus tokens CFN4!")

# Função principal que inicializa o bot
def main() -> None:
    # Obter o token do bot das variáveis de ambiente
    token = os.getenv("BOT_TOKEN")
    
    # Verificar se o token foi obtido com sucesso
    if token is None:
        logger.error("BOT_TOKEN não foi encontrado!")
        return
    
    # Criar o Updater e passar o token
    updater = Updater(token)

    # Obter o dispatcher para registrar os manipuladores de comandos
    dispatcher = updater.dispatcher

    # Adicionar os manipuladores de comandos
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("faucet", faucet))

    # Iniciar o bot
    updater.start_polling()

    # Rodar o bot até que o processo seja interrompido
    updater.idle()

if __name__ == '__main__':
    main()
