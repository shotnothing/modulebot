"""Summary

Attributes:
    logger (TYPE): Description
    PORT (TYPE): Description
    TOKEN (TYPE): Description
"""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
import os

PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Fetch token
TOKEN = os.environ.get('token', None)

def start(update, context):
    """Start command handler
    
    Args:
        update (TYPE): Description
        context (TYPE): Description
    """
    update.message.reply_text('Hi!')

def help(update, context):
    """Summary
    
    Args:
        update (TYPE): Description
        context (TYPE): Description
    """
    update.message.reply_text(type(update))
    update.message.reply_text(type(context))

def dont_understand(update, context):
    """Summary
    
    Args:
        update (TYPE): Description
        context (TYPE): Description
    """
    update.message.reply_text("Sorry, I don't understand {update.message.text}")

def error(update, context):
    """Summary
    
    Args:
        update (TYPE): Description
        context (TYPE): Description
    """
    logger.warning('[Error] Update "{update}" caused error "{context.error}"')

def main():
    """Summary
    """
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, dont_understand))

    # log errors
    dp.add_error_handler(error)

    # start bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://modulebotservice.herokuapp.com/' + TOKEN)

    updater.idle()

if __name__ == '__main__':
    main()