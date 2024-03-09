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
with open('input.txt', 'r') as f:
    # Чтение файла поблочно
    block = f.read(1024)
    # Поиск шестнадцатеричных чисел в блоке
    matches = []
    i = 0
    while i < len(block):
        if block[i].isdigit() or block[i].isalpha():
            j = i + 1
            while j < len(block) and (block[j].isdigit() or block[j].isalpha()):
                j += 1
            matches.append(block[i:j])
        i += 1
    # Перебор найденных чисел
    for match in matches:
        try:
            # Преобразование числа в шестнадцатеричное
            num = int(match, 16)
        except ValueError:
            print(f"{match} не является шестнадцатеричным числом")
            continue
        # Проверка, что число четное, не превышает 0x400 и первая цифра соответствует количеству цифр
        if num % 2 == 0 and num <= 0x400 and len(match) == int(match[0], 16):
            # Преобразование числа в строку
            num_str = ''
            for digit in match:
                if digit in digit_to_word:
                    num_str += digit_to_word[digit] + ' '
                else:
                    num_str += digit + ' '
            # Вывод числа и его прописного представления
            print(f"{match}: {num_str}", end='')
        else:
            print(f"{match} не удовлетворяет условию задачи", end='')
    # Чтение оставшихся блоков файла
    while block:
        block = f.read(1024)
        matches = []
        i = 0
        while i < len(block):
            if block[i].isdigit() or block[i].isalpha():
                j = i + 1
                while j < len(block) and (block[j].isdigit() or block[j].isalpha()):
                    j += 1
                matches.append(block[i:j])
            i += 1
        for match in matches:
            try:
                num = int(match, 16)
            except ValueError:
                print(f"{match} не является шестнадцатеричным числом")
                continue
            if num % 2 == 0 and num <= 0x400 and len(match) == int(match[0], 16):
                num_str = ''
                for digit in match:
                    if digit in digit_to_word:
                        num_str += digit_to_word[digit] + ' '
                    else:
                        num_str += digit + ' '
                print(f"{match}: {num_str}", end='')
            else:
                print(f"{match} не удовлетворяет условию задачи", end='')