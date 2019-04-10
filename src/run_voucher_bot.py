import argparse
import voucher_bot

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ejecucion del bot servicio')
    parser.add_argument('--token',  help='el token del bot')
    parser.add_argument('--api',  help='la url de la API')
    voucher_bot.VoucherBot(parser.parse_args().token, parser.parse_args().api).start_pooling()
