import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import Bot_functions

get_token = open("token.txt", "r")
token = get_token.readline()

calculator_bot = vk_api.VkApi(token=token)
id_list = []  # список для хранения id пользователей
bot_commands = (' "+ - * / ^ ()" ')


def reply(user_id, write_msg):  # Функция ответа
    calculator_bot.method('messages.send', {'user_id': user_id, 'message': write_msg, 'random_id': 0})


def is_integer(n):
    """ проверка числа на целочисленность """

    try:
        if n - int(n) == 0: 
            n = int(n)    
        
        else: 
            pass    
    
    except ValueError:
        pass

    return n


def answer(text):
    """ Получение ответа """

    try:
        # попытка вычисления ответа
        ans = Bot_functions.postfix_eval(text) 
    
    except UnboundLocalError:
        ans = "Я вас не понял, введите пример"

    return ans


longpoll = VkLongPoll(calculator_bot)  # подключение бота к longpoll серверу
while True:
    
    for message in longpoll.listen():
    
        if message.type == VkEventType.MESSAGE_NEW:
    
            if message.to_me:  # сообщение боту
                
                # ловим нового пользователя и добавляем id в список
                if message.user_id not in id_list:
                    
                    id_list.append(message.user_id)
                    # отправка первого сообщения
                    write_msg = "Привет, введите пример\nКоманды бота: " + bot_commands
                    reply(message.user_id, write_msg)
                    # вывод в консоль информации от пользователя
                    Bot_functions.information_from_user(message.user_id, message.text)
                
                else:  # пользователь не новый
                    
                    write_msg = answer(message.text)  # вызов функции подсчета для текста сообщения
                    reply(message.user_id, is_integer(write_msg))  # отправка ответа
            else:
                Bot_functions.information_from_me(write_msg)  # вывод в консоль информации от бота
