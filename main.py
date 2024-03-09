digit_to_word = {
    '0': 'ноль',
    '2': 'два',
    '4': 'четыре',
    '6': 'шесть',
    '8': 'восемь',
    'A': 'десять',
    'C': 'двенадцать',
    'E': 'четырнадцать'
}

with open('num1.txt', 'r') as f:
    # Чтение файла построчно
    lines = f.readlines()

    # Перебор строк
    for line in lines:
        # Разделение строки на лексемы
        lexemes = line.split()

        # Перебор лексем
        for lexeme in lexemes:
            try:
                # Преобразование лексемы в шестнадцатеричное число
                num = int(lexeme, 16)
            except ValueError:
                print(f"{lexeme} не является шестнадцатеричным числом")
                continue

            # Проверка, что число четное, не превышает 0x400 и первая цифра соответствует количеству цифр
            if num % 2 == 0 and num <= 0x400 and lexeme[0] in '13579BDF':
                # Преобразование числа в строку
                num_str = ''
                for digit in lexeme:
                    if digit in digit_to_word:
                        num_str += digit_to_word[digit] + ' '
                    else:
                        num_str += digit + ' '

                # Вывод числа и его прописного представления
                print(f"{lexeme}: {num_str}")
            else:
                print(f"{lexeme} не удовлетворяет условию задачи")
