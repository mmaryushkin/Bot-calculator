import datetime
from Stack import Stack

def is_number(x: str):
    """
    Функция возвращает True, если строка является числом, и False, если это не так
    """
    
    try:
        x = float(x)
        return True

    except ValueError:
        return False


priority = {"^": 1, "*": 2, "/": 2, "+": 3, "-": 3} # приоритет математических операций

def calculate(op, op1, op2):
    """ Вычисление """
    
    if op == "/":
        return op1 / op2
    if op == "*":
        return op1 * op2
    if op == "-":
        return op1 - op2
    if op == "+":
        return op1 + op2
    if op == "^":
        return op1 ** op2


def upgrade_expression(s: str):
    """ преобразование строки математического выражение без пробелов
    возвращает массив, элементы которого числа и операции примера """
    
    expression = ''
    num = '0123456789.'
    operations = '+-/*^()'
    
    for e in s: 
        
        if e in num: # цифры
            expression += e 
        
        elif e in operations: # знаки с пробелами
            expression += ' ' + e + ' '
    
    return expression.split()


def to_postfix(s: str):
    """ Преобразование инфиксного выражения в постфиксную запись """

    a = upgrade_expression(s)
    postfix = [] # список для записи постфиксного выражения
    opstack = Stack([]) # стек для операций

    for i in a:
        
        if is_number(i):
            postfix.append(i)
        
        else:
            
            if i == '(':
                opstack.push(i)
            
            elif i == ')':
                # по очереди достаем все элементы в скобках
                op = opstack.get_last()
                while op != '(':
                    postfix.append(op)
                    op = opstack.get_last()
            
            else:
                if not opstack.is_empty():
                    
                    if opstack.top() == '(':
                        opstack.push(i)
                   
                    else:
                    
                        if priority[i] >= priority[opstack.top()]: # приоритет операции больше или равна приоритету последней операции в стеке
                            postfix.append(opstack.get_last()) # выталкиваем в выражение последнюю операцию
                            opstack.push(i)
                        
                        else:
                            opstack.push(i)
                else:
                    opstack.push(i)
    
    while not opstack.is_empty():
        postfix.append(opstack.get_last())
    
    return postfix


def postfix_eval(s: str):
    """ Вычисление постфиксного выражения """

    a = to_postfix(s)
    stack = Stack([])

    for i in a:
        
        if is_number(i):
            stack.push(float(i))
        else:
            x = stack.get_last()
            y = stack.get_last()
            result = calculate(i, y, x)
            stack.push(result)
    
    return result


def information_from_user(muid, text): 
    """ Информация от пользователя """

    print("\nПользователь:\n")
    print("id: " + str(muid))
    print("текст сообщения: " + str(text))
    print("сообщение принято в: " + str(datetime.datetime.now()) + "\n\n")


def information_from_me(text):
    """ Информация от бота """
    
    print("Бот:\n")
    print("текст сообщения: " + str(text))
    print("сообщение отправлено в: " + str(datetime.datetime.now()) + "\n\n")