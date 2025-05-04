# Программа для распознавания речи (расшифровка аудио)
# Файл должен быть в формате .wav
# Установить библиотеку: pip install SpeechRecognition

import speech_recognition as sr

FILE = "audio.wav"  # Путь к аудиофайлу
# или путь к файлу FILE = r"C:\Users\Documents\audio.wav"

r = sr.Recognizer()  # Создаём объект для распознавания
with sr.AudioFile(FILE) as source:  # Открываем аудиофайл
    audio = r.record(source)  # Считываем всё аудио

try:
    # Пробуем распознать аудио через Google API
    text = r.recognize_google(audio, language="ru-RU")
    print(text)  # Выводим текст
except sr.UnknownValueError:
    # Если речь не распознана
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    # Если ошибка при запросе к сервису
    print(f"Could not request results from Google Speech Recognition service; {e}")
