import logging
import urllib2
from telegram.ext import Updater
from telegram.ext import CommandHandler

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class VoucherBot():
    ''' Esta clase contiene todo lo necesario para operar el bot '''

    def __init__(self, token, api_url):
        self._updater = Updater(token=token)
        self._url = api_url
        self._dispatcher = self._updater.dispatcher
        self.start_handler = CommandHandler('start', self.start)
        self.voucher_handler = CommandHandler('voucher', self.voucher)
        self._dispatcher.add_handler(self.start_handler)
        self._dispatcher.add_error_handler(self.error_handler)

    def start(self, bot, update):
        ''' Mensaje inicial del voucher '''
        bot.send_message(chat_id=update.message.chat_id,text='''Bienvenido a 
        Voucher-Unlp-Bot, el bot que recupera el voucher del Wifi. 
        Ingrese /voucher para obtener el voucher del dia''')
    
    def voucher(self, bot, update):
        ''' Devuelve el voucher '''
        bot.send_message(chat_id=update.message.chat_id,text=VoucherHttpRetriever.retrieve(self.api_url()))

    def start_pooling(self):
        self._updater.start_polling()
        self._updater.idle()

    def error_handler(self, bot, error):
        bot.send_message(text='Ha ocurrido un error inesperado.')


    def api_url(self):
        return self._url + "/voucher?url=http://lafuenteunlp.com.ar/web/"

class VoucherHttpRetriever():
    ''' recupera el voucher mediante http '''

    @staticmethod
    def retrieve(url):
        _contents = urllib2.urlopen(url).read()

