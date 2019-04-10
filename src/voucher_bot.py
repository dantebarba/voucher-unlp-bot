import logging
import urllib2
from telegram.ext import Updater
from telegram.ext import CommandHandler

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class VoucherBot():
    ''' Esta clase contiene todo lo necesario para operar el bot '''
    _url = "http://localhost:5000/voucher?url=http://lafuenteunlp.com.ar/web/"

    def __init__(self, token):
        self._updater = Updater(token=token)
        self._dispatcher = self._updater.dispatcher
        self.start_handler = CommandHandler('start', self.start)
        self.voucher_handler = CommandHandler('voucher', self.voucher)
        self._dispatcher.add_handler(self.start_handler)

    def start(self, update, context):
        ''' Mensaje inicial del voucher '''
        context.bot.send_message(chat_id=update.message.chat_id, text='''Bienvenido a 
        Voucher-Unlp-Bot, el bot que recupera el voucher del Wifi. 
        Ingrese /voucher para obtener el voucher del dia''')
    
    def voucher(self, update, context):
        ''' Devuelve el voucher '''
        context.bot.send_message(chat_id=update.message.chat_id, text=VoucherHttpRetriever.retrieve(self._url))

    def start_pooling(self):
        self._updater.start_polling()

class VoucherHttpRetriever():
    ''' recupera el voucher mediante http '''

    @staticmethod
    def retrieve(url):
        _contents = urllib2.urlopen(url).read()

