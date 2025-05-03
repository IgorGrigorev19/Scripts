import os

# Путь к директории
DIRECTORY = r"C:\PycharmProjects\my1project\1"

print("Рабочая папка:", DIRECTORY)
if os.path.exists(DIRECTORY):
    print("Путь существует ✅")
else:
    print("Путь НЕ найден ❌")


def rename_file(find_dirq):
    for root, dirs, files in os.walk(find_dirq):
        for name in files:
            rename_files(root, name)


def rename_files(root, name):
    print("Папка:", root)
    print("Имя файла:", name)

    valid_name = get_valid_name(name)
    print("Новое имя файла:", valid_name)
    print("Старое имя файла:", name)
    print("---------")

    old_file = os.path.join(root, name)
    print("Старый путь:", old_file)

    new_file = os.path.join(root, valid_name)
    print("Новый путь:", new_file)

    os.rename(old_file, new_file)
    print("✅ Файл переименован:", name, "→", valid_name)


def get_valid_name(name):
    name = name.replace("9", "night")
    name = name.replace(".jpg", ".png")
    return name


rename_file(DIRECTORY)