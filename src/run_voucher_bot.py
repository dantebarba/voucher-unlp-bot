import argparse
import voucher_bot

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ejecucion del bot servicio')
    parser.add_argument('--token',  help='el token del bot')
    voucher_bot.VoucherBot(parser.parse_args().token).start_pooling()
