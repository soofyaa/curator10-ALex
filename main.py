import telebot

bot = telebot.TeleBot('6412037605:AAHcflF1lC-0kzAseIG96OSyycr0zyNI2WY')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Ну это...для начала...с Праздником тебя!')


@bot.message_handler(commands=['vopros'])
def main(message):
    bot.send_message(message.chat.id, 'Так что? Мурка или начнем с кузнечика?')


@bot.message_handler(commands=['kuznechik'])
def main(message):
    bot.send_message(message.chat.id, 'Кхе, это и я так могу! \nА чо ж сыграть то? \n*Мурку!*', parse_mode='Markdown')


@bot.message_handler(commands=['murka'])
def main(message):
    bot.send_message(message.chat.id, 'Вот! \nСовсем другое дело!')


@bot.message_handler(commands=['bye'])
def main(message):
    bot.send_message(message.chat.id, 'Подпишись на мою [группу!](https://vk.ru/club2) \nИ заглядывай еще!')


bot.infinity_polling()
