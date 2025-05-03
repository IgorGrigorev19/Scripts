import os
import time
from datetime import datetime

# Количество секунд в сутках
TIME_BORDER = 86400
DATE_FORMAT = "%Y-%m-%d-%H-%M-%S"

# Проверка Директории
CHECK_DIRECTORY = r"C:\PycharmProjects\my1project"

# ПУТЬ К ФАЙЛУ ЛОГУ
FILE_LOG = r"C:\PycharmProjects\my1project\FindVirus\log.txt"

def clear_log():
    with open(FILE_LOG, 'w') as f:
        pass  # просто очищает

def find_virus(find_directory):
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            file = os.path.join(root, name)
            if check(file):
                add_to_log(file)

def check(file):
    current_ts = time.time()
    change_time = get_change_time(file)
    return current_ts - change_time < TIME_BORDER

def get_change_time(file):
    stats = os.stat(file)
    return max(stats.st_atime, stats.st_mtime, stats.st_ctime)

def add_to_log(file):
    adding_string = f"{file}: {datetime.fromtimestamp(get_change_time(file)).strftime(DATE_FORMAT)}"
    with open(FILE_LOG, 'a') as f:
        f.write(adding_string + '\n')

# 🟢 выносим вызовы ВНЕ функции:
clear_log()
find_virus(CHECK_DIRECTORY)
