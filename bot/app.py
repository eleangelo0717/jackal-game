from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import os
import logging
import commands
import declaration

load_dotenv()

TOKEN = os.getenv('TGM_BOT_TOKEN')
PROXY_URL = os.getenv('PROXY_URL')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def main():
    request_kwargs = {'read_timeout': 6, 'connect_timeout': 7}
    if PROXY_URL is not None:
        request_kwargs = {
            'proxy_url': PROXY_URL
        }

    updater = Updater(token=TOKEN, request_kwargs=request_kwargs)

    updater.dispatcher.add_handler(CommandHandler('hello', commands.start))
    updater.dispatcher.add_handler(CommandHandler('start', commands.start))
    updater.dispatcher.add_handler(CommandHandler('status', commands.status))
    updater.dispatcher.add_handler(CommandHandler('stop', commands.stop))
    updater.dispatcher.add_handler(CommandHandler('clear', commands.clear))
    updater.dispatcher.add_handler(CommandHandler('view', commands.view))
    updater.dispatcher.add_handler(CommandHandler('declaration', commands.check_declaration))

    updater.dispatcher.add_handler(CommandHandler(['edit_date_from', 'edit_date_to'], commands.edit))
    updater.dispatcher.add_handler(CommandHandler([f'edit_{key}' for key in declaration.docFields.keys()], commands.edit))

    updater.dispatcher.add_handler(MessageHandler(Filters.text, commands.text_input))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

