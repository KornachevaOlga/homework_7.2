import os


def custom_write(file_name, strings):
    strings_positions = {}
    current_position = 0

    if os.path.isfile(file_name):
        with open(file_name, 'a', encoding='utf-8') as file:
            for idx, string in enumerate(strings, start=1):
                # Записываем каждую строку с переносом
                file.write(string + '\n')

                # Фиксируем текущую позицию строки
                strings_positions[(idx, current_position)] = string
                current_position = file.tell()  # Обновляем позицию после записи

        return strings_positions
    else:
        print("Файл не существует.")
        return None


# Список строк для записи
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

# Вызов функции и вывод результата
result = custom_write('test.txt', info)
if result:
    for elem in result.items():
        print(elem)