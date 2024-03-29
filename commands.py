# globalsDict Это списк всех переменных в cmdd.py, это нужно например для взаимодействия с функциями или ткинтером
# Он передаётся как последний аргумент
# _ Нужно чтобы избежать конфликтов с другими функциями, название функции это то, что нужно будет вводить в cmd (Без _)

from os import system
from time import sleep
from string import ascii_lowercase
# import subprocess

# def system_call(command):
#     result = subprocess.run([command], stdout=subprocess.PIPE, shell=True)
#     return result.stdout.decode('utf-8')

def checkCommand(cmd, *args):  # Проверка правильности введёной команды (Не обязательно, делается вручную)
    if cmd == 'shampoo':
        via = args[0]
        mark = args[1]
        ml = args[2]
        flush = args[3]
        return True if via == 'via' and flush == 'true' or flush == 'false' else False

    elif cmd == 'connect':
        try:
            ip = args[0]
            user = args[1]
            q = ip.split('.')
            for w in q:
                w = int(w)
                if not w <= 255 and w >= 0:
                    return False
        except Exception:
            return False
        return True

def _official(*args):
    return "Официальный файл commands.py"

# Настроки команд (Можно менять)

PORT = 10000 # Порт по умолчанию


# Делать команды ниже.     _название(*args)

def _encry(*args):
    from random import randint
    try:
        text = args[0]
    except Exception:
        return 'SyntaxError'

    alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", 
            "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]

    alphabet = ascii_lowercase

    publisher = text # исходный текст
    res = '' # блок в шестнадцатиричной системе
    block = '' # строка блоков
    key_dec = '' # строка ключей в dec
    key = '' # ключ 
    chain = '' # это итоговая цепочка
    count = 0 # первый счетчик для перебора букв и их намеров
    method = 0.00 # переменная для превращения каждого элемената в ирацианально число
    spam = 0 # блок в восьмеричной/десятичной системе
    rand1 = 0 # случайное число
    temp = [] # список для записи чисел после деления на π
    subsequence = [] # список с исходными намерами букв домноженый на 1000
    randl1 = [] # список ключей
    aelist = [] # список блоков
    pi = 3.141592653589793 # π

    #Перевод чисел в числовую последовательность по афавиту с коофициентом 1000
    def translation(count, subsequence):
        for i in publisher:
            while i != alphabet[count]:
                count +=1
            if i == alphabet[count]:
                subsequence.append((count+1)*1000)
                subsequence.append(0)
                count = 0

    # деление на π и округление до целого числа с кооффициентом 100
    def irationality(subsequence, method, temp):
        for y in subsequence:
            if y != 0:
                method = y/pi
                temp.append(round(method*100))
                #temp.append(0)

    # шифрование блоков и генерация ключей        
    def rationality(temp, rand1, randl1, spam, res, aelist):
        for u in temp: # u это один блок
            rand1 = randint(3,9) # рандомное число
            randl1.append(rand1) # добавляем это число в список 
            spam = int(oct(u)[2:]) # переводим u в восьмеричную систему
            spam = spam*rand1 # домнажаем на это то рандомное число
            spam = int(oct(spam)[2:]) # переводим это обратно в восьмеричную систему
            res = f'{spam:x}' # и теперь как десятичеую переводим в шестнадцатиричную
            aelist.append(res) # добавляем этот блок в список
    

    # Запуск системы

    def start():     
        translation(count=count, subsequence=subsequence)
        irationality(subsequence=subsequence, method=method, temp=temp)
        rationality(temp=temp, rand1=rand1, randl1=randl1, spam=spam, res=res, aelist=aelist)
        

    start()
    # генерация цепи              
    for t in randl1:
        key_dec += str(t)

    for z in aelist:
        block += str(z)
                    
    key = f'{int(key_dec):x}'
    chain = str(block) + ':' + str(key)
    return chain, '--fast'

def _decry(*args):
    try:
        crypted = args[0]
        text = args[1]
    except Exception:
        return 'SyntaxError'
    encryption = crypted

    alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", 
                "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]

    publisher = text # исходный текст
    res = '' # блок в шестнадцатиричной системе
    block = '' # строка блоков
    spam = 0 # блок в восьмеричной/десятичной системе
    count = 0 # первый счетчик для перебора букв и их намеров
    count1 = 0 # второй счетчик для домножения temp
    method = 0.00 # переменная для превращения каждого элемената в ирацианально число
    temp = [] # список для записи чисел после деления на π
    subsequence = [] # список с исходными намерами букв домноженый на 1000
    keyl = [] # строка ключей в шестнадцатиричной сисетме
    trash = [] # строка блоков в шестнадцатиричной системе
    aelist = [] # список всех блоков домноженых на коофициенты
    key_dec_l = [] # список ключей в десятичной сисеме
    conf = 0 # в какой их списков пойдет символ
    pi = 3.141592653589793 # π

    #Перевод чисел в числовую последовательность по афавиту с коофициентом 1000
    try:
        for i in publisher:
            while i != alphabet[count]:
                count +=1
            if i == alphabet[count]:
                subsequence.append((count+1)*1000)
                subsequence.append(0)
                count = 0
    except Exception:
        return 'Можно юзать только маленькие рус буквы', '--fast'

    # деление на π и округление до целого числа с кооффициентом 100

    for y in subsequence:
        if y != 0:
            method = y/pi
            temp.append(round(method*100))
            #temp.append(0)
            
            
    # тут мы разделяем эдементы до двоеточия и после
    for z in encryption:
        if conf == 0:
            trash.append(z) # до
            if z == ':':
                conf = 1
        elif conf == 1:
            keyl.append(z) # после
            
    key_hex = (''.join(keyl))
    key_dec = int(key_hex, 16)

    # переводим десятичные ключи в список 
    for c in str(key_dec):
        key_dec_l.append(c)
        
    # генерируем блоки из добытых ключей
    for u in temp:
        spam = int(oct(u)[2:])
        spam = int(spam) * int(key_dec_l[count1])
        count1 += 1
        spam = int(oct(spam)[2:])
        res = f'{spam:x}'
        aelist.append(res)
        
    # переводим блоки в строку
    for p in aelist:
        block += str(p)
        
    # создаем цепочку   
    chain = str(block) + ':' + str(key_hex)

    if chain == encryption:
        return "Succecful"
    else:
        return "Failed"

# def _net(*args):
#     try:
#         action = args[0]
#     except Exception:
#         return '..действие? SyntaxErr'

#     match action:                               # Если сможешь реализовать харош
#         case 'fix':
#             act = args[1]
#             try:
#                 PORT = args[2]
#             except Exception:
#                 pass

#             # if act == 'get':
#             #     return system(f'netstat -o | findstr :{PORT}'), '--fast'  # Ищем процесс, который использует наш порт
#             return system(f'taskkill -pid {PORT} /f')  # Завершаем этот процесс

def _taskkill(*args):
    try:
        pid = args[0]
        gl = args[-1]
    except Exception:
        return 'SyntaxError'
    system(f'taskkill -pid {pid} /f')
    return 'Done'

def _shampoo(*args):
    try:
        via = args[0]
        mark = args[1]
        ml = args[2]
        flush = args[3]
        
    except Exception:
        return 'SyntaxError1'
    if not checkCommand('shampoo', *args):  #
        return 'SyntaxError'

    if flush == 'true':
        return f'FLUSHED SHAMPOO via {mark}, {ml} Ml'
    else:
        return f'RUN SHAMPOO -> {mark}, {ml} Ml'

def _connect(*args):
    try:
        ip = args[0]
        user = args[1]
    except Exception:
        return 'SyntaxError'
    if not checkCommand('connect', *args):
        return 'connection refused! Incorrect IPv4 Adress'

    return f'connecting to {user} via IPv4: {ip}'    

def _test(*args):  # Для различных тестирований
    try:
        one = args[0]
        two = args[1]
        globalList = args[2]
    except Exception:
        return 'Err'
    return f'{one}; {two} /\n{globalList}'

def _wifi(*args):
    try:
        user = 'uff'      # Пользователь
        action = args[0]  # on / off
        time = args[1]    # Время, на которое отключиться wifi
        wait = args[2]    # Сколько ждать перед отключение wifi
        globalsDict = args[3]
        root = globalsDict['root']
        send = globalsDict['send']
    except Exception:     # Пример:     wifi off 2 0
        return 'ERR: Синтаксис Пример: wifi off 2 0'

    if action == 'on': # Включить wifi
        send('on 0')
        return f'WiFi user={user} enabled'

    elif action == 'off': # Отключить wifi
        root.after(int(wait)*1000)       # Секунды -> миллисекунды
        print(f'Wait: {int(wait)*1000}') # Выводим сколько ждать
        send(f'off {time}')              # Посылаем запрос на отключение
        return f'WiFi user={user} disabled'

def _help(*args):
    try:
        command = args[0]
    except Exception:
        return """
        Команды в файле commands.py
        Команды: encry, decry, shampoo, connect, cls, test, wifi, kill
        Для помощи по отдельной команде введи: help <название команды>
        Левый Alt: запустить команду
        Правый Alt: очистить строку ввода
        Ecs: выйти
        Enter: запустить команду
        """
    if command == 'encry':
        return "encry: Используется для шифрования слова. Использование: encry <слово>"
    elif command == 'decry':
        return 'Используется для проверки совпадает ли зашифрованный текст с исходным. Использование: decry <шифр> <исходное слово>'
    elif command == 'shampoo':
        return 'Команда для развлечения. Использование: shampoo via <марка> <объём (число)> <true/false>'
    elif command == 'connect':
        return "Типо подключение (На самом деле нет) Использование: connect <ip> <user>\nПример ip: 192.52.11.253"
    elif command == 'cls':
        return 'Очистка поля вывода и ввода. Использование: cls'
    elif command == 'test':
        return 'Команда для теста. Использование: test <arg1> <arg2>'
    elif command == 'wifi':
        return 'Не обращай внимания, это тебе не нужно.'
    elif command == 'kill':
        return "Выход"
    elif command == 'taskkill':
        return 'Завершение процесса. Использование: taskkill <pid>'
    else:
        return """
        Команды в файле commands.py
        Команды: encry, decry, shampoo, connect, cls, test, wifi, kill
        Для помощи по отдельной команде введи: help <название команды>
        Левый Alt: запустить команду
        Правый Alt: очистить строку ввода
        Ecs: выйти
        Enter: запустить команду
        """, '--fast'

if __name__ == '__main__':
    print('=\n=\n=\n=\n=\n=\n=\n=\n=\n=\n====================\nЗапускать файл cmdd.py')
    for i in range(5):
        print('\\', end='')
        print('\r',end='                  ')
        sleep(0.1)
        print('|', end='')
        print('\r',end='                  ')
        sleep(0.1)
        print('/', end='')
        print('\r',end='                  ')
        sleep(0.1)
        print('|', end='')
        print('\r',end='                  ')
        sleep(0.1)
        

