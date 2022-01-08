import argparse


def get_cmdline_args():
    parser = argparse.ArgumentParser(
        description='CLI interface for Price Formatter'
    )
    parser.add_argument('price', help='price string')
    return parser.parse_args()


def format_price(price):
    if not isinstance(price, bool):
        try:
            float_price = round(float(price), 2)
            if float_price.is_integer():
                return '{:,}'.format(int(float_price)).replace(',', ' ')
            else:
                return '{:,.2f}'.format(float_price).replace(',', ' ')
        except (ValueError, TypeError):
            return None


if __name__ == '__main__':
    args = get_cmdline_args()
    print(format_price(args.price))
