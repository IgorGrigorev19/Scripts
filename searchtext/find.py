import os

# 👉 Путь к папке, в которой будем искать файлы
DIRECTORY = r"C:\PycharmProjects\my1project\ContentFiles\Test"

# 👉 Строка, которую нужно найти в файлах
FIND_STRING = "простострок"

def find_string_in_file(file, find_string):
    """
    Функция открывает файл, читает весь текст
    и проверяет, есть ли в нём искомая строка.
    Если строка найдена — вызывает print_find_info().
    """
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()  # читаем всё содержимое файла
    index = content.find(find_string)  # ищем индекс первого вхождения строки
    if index != -1:
        print_find_info(file, content, find_string)  # если нашли → печатаем инфо

def print_find_info(file, content, find_string):
    """
    Функция печатает информацию о файле, где найдена строка.
    """
    print(f"✅ Найдена строка '{find_string}' в файле: {file}")
    # можно дополнить выводом позиции, фрагмента текста и др.

def find(find_directory, find_string):
    """
    Функция обходит папку (и все вложенные),
    и проверяет каждый файл через find_string_in_file().
    """
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            filepath = os.path.join(root, name)  # получаем полный путь к файлу
            find_string_in_file(filepath, find_string)  # проверяем файл

# 👉 Запускаем поиск
find(DIRECTORY, FIND_STRING)
