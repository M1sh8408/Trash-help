from config_bot import TOKEN_bot

import telebot

bot = telebot.TeleBot(TOKEN_bot)

plastick = ['пакет',"ручка","одноразовый стакан","лопатка для песочницы"]
paper = ["коробка от пиццы","коробка от молока","бумажный самолётик"]
metal = ["жестяная банка","проволока","консервная банка","жестяной лист"]
glass = ["разбитое зеркало","банка","рабитый стакан","разбитая кружка"]
unreal = ['банан',"яблоко","апельсин","груша","апельсин","банановая кожура"]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет я бот который поможет тебе сортировать мусор')

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,'Спрашивай у бота какой мусор куда выкидывать. Просто напиши слово которое тебе нужно.')

@bot.message_handler(commands=['proof'])
def proof(message):
    print('Бот пруфанул')
    bot.reply_to(message, f'Да это бот Михаила Мякинькова ')

@bot.message_handler(func=lambda message: True)
def trasher(message):
    
    print('Сообщение пришло')
    if message.text.lower() in plastick:
        bot.send_message(message.chat.id,'Выкидывай это в пластиковые отходы')
        

    elif message.text.lower() in paper:
        bot.send_message(message.chat.id,'Выкидывай это в бумажные отходы')


    elif message.text.lower() in metal:
        bot.send_message(message.chat.id,'Выкидывай это в металлические отходы')


    elif message.text.lower() in glass:
        bot.send_message(message.chat.id,'Выкидывай это в стеклянные отходы')


    elif message.text.lower() in unreal:
        bot.send_message(message.chat.id,'Это невозможно переработать выкидывай в органические отходы')

    elif message.text.lower() == 'бутылка':
        bot.send_message(message.chat.id,'Она может быть и из пластика и из стекла')

    else:
        bot.send_message(message.chat.id,'Либо это не мусор, либо этого нет в наших списках, простите')
        print('Ктото хотел узнать про предмет которого нет в списках')

bot.polling()
