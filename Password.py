print('Please enter the password. He must сontain One number, One upper symbol, One special symbol')
x = str(input())
if len(x) <= 8: # Сначала проходит проверка по количеству символов. Остальные проверки делать смысла нет.
    print('Not enough symbols')
else:
    def check_password(s):
        return any(x.isdigit() for x in s) and any(x.isupper() for x in s) and any(x.isalpha() for x in s) # Генератор списков, 19-21 ЕГЭ по информатике. 
        # And нужен, чтобы все Три были True, в ином случае мы получим False.
        # Сначала идет проверка цифра ли для каждого символа, потом вверхний ли это индекс, а затем специальный ли это символ. 
    if check_password(x): # Если у нас прошла проверка, мы получили при Хотя бы Одном совпадении True и переходим дальше
        print('Please re-enter password')
        y = str(input())
        if y == x: # Проверка одинаковости строк по наполнению
            print('Well done!')
        else:
            print('Wrong password!')
    else:
        print('Missing сontains')