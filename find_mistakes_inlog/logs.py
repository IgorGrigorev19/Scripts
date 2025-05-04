# Импортируем модуль для отправки почты через SMTP
import smtplib
# Импортируем классы для создания письма (MIME)
from email.mime.text import MIMEText

# Путь к файлу лога
FILE = "error.log"
# Настройки SMTP сервера
SERVER = "smtp.yandex.ru"   # Адрес SMTP сервера (через него отправляем почту)
PORT = 587                  # Порт SMTP сервера (587 — стандартный порт для TLS)
LOGIN = "test"              # Логин для входа на SMTP сервер (почтовый ящик без @yandex.ru)
PASSWORD = "PASSWORD"       # Пароль от почтового ящика (или пароль приложения)
TO = "<EMAIL>"            # Кому отправлять письмо
FROM_EMAIL = "test@yandex.ru"  # От кого письмо
TEXT_TYPE = "html"        # Тип письма (HTML)

# Функция для проверки ошибок в лог файле
def check_errors(file):
    f = open(file, "r")          # Открываем файл для чтения
    lines = f.readlines()        # Читаем все строки файла
    f.close()                    # Закрываем файл

    notices = 0                  # Счётчик уведомлений
    warnings = 0                 # Счётчик предупреждений
    errors = 0                   # Счётчик ошибок

    for line in lines:           # Проходимся по каждой строке
        print(line.strip())       # Выводим строку в консоль (убираем лишние переводы строк)
        if "php7:notice" in line:   # Если в строке есть notice
            notices += 1
        elif "php7:warn" in line:   # Если есть warn
            warnings += 1
        elif "php7:error" in line:  # Если есть error
            errors += 1

    # Если есть хотя бы одна ошибка/предупреждение/уведомление, отправляем отчёт
    if notices or warnings or errors:
        send_report(notices, warnings, errors)

# Функция для формирования и отправки отчёта
def send_report(notices, warnings, errors):
    # Формируем HTML-текст отчёта
    message = "<div>Типы ошибок и их количество:<br />"
    message += "<b>Notices:</b> " + str(notices) + "<br />"
    message += "<b>Warnings:</b> " + str(warnings) + "<br />"
    message += "<b>Errors:</b> " + str(errors) + "</div>"

    # Вызываем функцию отправки письма
    send_email(TO, "Есть ошибки в логах", message)

# Функция для отправки email
def send_email(to, subject, message):
    # Создаём письмо с указанным текстом, форматом и кодировкой
    msg = MIMEText(message, TEXT_TYPE, "utf-8")
    msg['Subject'] = subject    # Тема письма
    msg['From'] = FROM_EMAIL    # От кого письмо
    msg['To'] = to              # Кому письмо

    # Подключаемся к SMTP серверу
    smtp = smtplib.SMTP(SERVER, PORT)
    smtp.starttls()             # Запускаем шифрование
    smtp.login(LOGIN, PASSWORD) # Логинимся
    smtp.send_message(msg)      # Отправляем письмо
    smtp.quit()                 # Закрываем соединение

# Запуск проверки ошибок
check_errors(FILE)
