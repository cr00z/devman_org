import telebot
from jinja2 import Template

from base import app
from models import Items, Choices


if not app.config['BOT_TOKEN']:
    raise Exception('BOT_TOKEN should be specified')
bot = telebot.TeleBot(app.config['BOT_TOKEN'])

with open('templates/catalog.md', 'r', encoding="utf-8") as catalog_file:
    catalog_tmpl = Template(catalog_file.read())

with open('templates/greetings.md', 'r', encoding="utf-8") as greetings_file:
    greetings_tmpl = Template(greetings_file.read())


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, greetings_tmpl.render())


@bot.message_handler(commands=['menu'])
def show_catalog(message):
    catalog_list = Items.query.join(Choices).all()
    bot.send_message(
        message.chat.id,
        catalog_tmpl.render(catalog=catalog_list),
        parse_mode='Markdown'
    )


if __name__ == '__main__':
    bot.polling(none_stop=True)
