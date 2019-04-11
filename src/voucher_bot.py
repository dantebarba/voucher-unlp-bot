import requests
import urllib2
from telegram.ext import Updater
from telegram.ext import CommandHandler

class VoucherBot():
    ''' Esta clase contiene todo lo necesario para operar el bot '''

    def __init__(self, token, api_url):
        self._updater = Updater(token=token)
        self._url = api_url
        self._dispatcher = self._updater.dispatcher
        self.start_handler = CommandHandler('start', self.start)
        self.voucher_handler = CommandHandler('voucher', self.voucher)
        self._dispatcher.add_handler(self.start_handler)
        self._dispatcher.add_handler(self.voucher_handler)
        self._dispatcher.add_error_handler(self.error_handler)

    def start(self, bot, update):
        ''' Mensaje inicial del voucher '''
        bot.send_message(chat_id=update.message.chat_id,text='''Bienvenido a Voucher-Unlp-Bot, el bot que recupera el voucher del Wifi. 
Ingrese /voucher para obtener el voucher del dia''')
    
    def voucher(self, bot, update):
        ''' Devuelve el voucher '''
        content = requests.get(self.api_url()).content
        bot.send_message(chat_id=update.message.chat_id,text=content)

    def start_pooling(self):
        self._updater.start_polling()
        self._updater.idle()

    def error_handler(self, bot, error):
        bot.send_message(text='Ha ocurrido un error inesperado.')


    def api_url(self):
        return self._url + "/voucher?url=http://lafuenteunlp.com.ar/web/"