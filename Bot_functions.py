import datetime
from Stack import Stack


def is_number(x: str):
    """ Функция возвращает True, если строка является числом, и False, если это не так """
    
    try:
        x = float(x)
        return True

    except ValueError:
        return False


"""
Вычисление примеров осуществляется через алгоритм решение математических выражений в постфиксной записи. 
(операция находится после операндов, например "2 2 +").
Пользователь присылает боту математический пример в инфиксной записи 
(операция находится между операндами, например "2 + 2").
Программа преобразует инфиксную запись примера в постфиксную, постфиксное выражение записывается в список.
Для вычисление ответа, из списка с постфиксной записью исходного математического выражения, вытаскиваются два числа и 
операция, вычисленное значение ставится на их место. Подсчет происходит, пока в списке не останется один элемент, 
который и является ответом примера.
"""

priority = {"^": 1, "*": 2, "/": 2, "+": 3, "-": 3}  # приоритет математических операций


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
        
        if e in num:  # цифры
            expression += e 
        
        elif e in operations:  # знаки с пробелами
            expression += ' ' + e + ' '
    
    return expression.split()


def to_postfix(s: str):
    """ Преобразование инфиксного выражения в постфиксную запись """

    a = upgrade_expression(s)
    postfix = []  # список для записи постфиксного выражения
    opstack = Stack([])  # стек для операций

    for i in a:
        
        if is_number(i):  # если элемент исходного выражение число, элемент добавляется в список
            postfix.append(i)
        
        else:  # если элемент исходного выражения операция или скобка
            if i == '(':  # если элемент исходного выражения открывающая скобка, элемент добавляется в стек
                opstack.push(i)
            
            elif i == ')':  # если элемент исходного выражения закрывающая скобка
                # по очереди записываем в список все элементы в скобках
                op = opstack.get_last()
                while op != '(':
                    postfix.append(op)
                    op = opstack.get_last()
            
            else:
                if not opstack.is_empty():
                    if opstack.top() == '(':  # если последний элемент стека открывающая скобка
                        opstack.push(i)  # операция добавляется в стек
                   
                    else:
                        if priority[i] >= priority[opstack.top()]:  # если приоритет операции больше или равен приоритету последней операции в стеке
                            postfix.append(opstack.get_last())  # выталкиваем в выражение последнюю операцию
                            opstack.push(i)  # добавляем в стек текущий элемент
                        else:  # иначе операция добавляется в стек
                            opstack.push(i)
                else:  # стек пустой
                    opstack.push(i)
    
    while not opstack.is_empty():  # пока в стеке есть элементы, добавляем их в список
        postfix.append(opstack.get_last())
    
    return postfix


def postfix_eval(s: str):
    """ Вычисление постфиксного выражения """

    a = to_postfix(s)
    stack = Stack([])

    for i in a:
        
        if is_number(i):  # если элемент списка число, добавляем в стек
            stack.push(float(i))
        else:  # если операция, достаем два элемента и вызываем функцию подсчета
            x = stack.get_last()
            y = stack.get_last()
            result = calculate(i, y, x)
            stack.push(result)  # добавляем в стек результат
    
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
