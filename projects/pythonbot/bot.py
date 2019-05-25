from telegram.ext import Updater, CommandHandler
PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет, человек по фамилии {}, хочешь знать ответ на это: {}?" format(update.message.chat.last_name, update.message.text)
    print(update.message)
    update.message.reply_text(user_text)

def main():
    mybot = Updater("768453628:AAHeNvlEQqNG6i2c8VgVvPmjhDRO32O7O5o", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    mybot.idle()

main()
