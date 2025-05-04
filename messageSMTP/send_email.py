#### Отправляем письма на E-mail
import smtplib  # библиотека для работы с SMTP (отправка почты)
from email.mime.text import MIMEText  # класс для создания текстового письма

# Константы для подключения к SMTP-серверу
SERVER = "smtp.yandex.ru"  # адрес SMTP-сервера Яндекса
PORT = 465  # порт для защищенного соединения (SSL)
LOGIN = "test"  # логин от твоей почты (без @yandex.ru, если логин = имя)
PASSWORD = "PASSWORD"  # пароль от почты
FROM_EMAIL = "test@yandex.ru"  # важно: здесь должно быть с @
TEXT_TYPE = "plain"  # plain = обычный текст, можно заменить на "html" если нужно

def send_email(to, subject, message):
    # Создаем объект MIMEText (само письмо)
    msg = MIMEText(message, TEXT_TYPE, "utf-8")
    msg['Subject'] = subject  # тема письма
    msg['From'] = FROM_EMAIL  # от кого (адрес отправителя)
    msg['To'] = to  # кому (адрес получателя)

    # Создаем SMTP-соединение через SSL (защищенное)
    smtp = smtplib.SMTP_SSL(SERVER, PORT)  # используем SMTP_SSL и порт 465
    smtp.login(LOGIN, PASSWORD)  # логинимся на сервере
    smtp.send_message(msg)  # отправляем письмо
    smtp.quit()  # закрываем соединение

# Вызов функции: отправляем письмо
send_email("to@example.com", "Тема письма", "Привет! Это тестовое сообщение.")  # укажи реальный email
