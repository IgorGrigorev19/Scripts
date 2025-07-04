#!/bin/bash

# ---------------------------------------------
#         MAX STRING FINDER SCRIPT
# ---------------------------------------------

echo "********* MAX STRING Script ********"

# Получаем имя файла из первого аргумента
file_name="$1"

# Проверка: доступен ли файл для чтения
if [ -r "$file_name" ]; then

    # Извлекаем все строковые данные из файла с помощью команды `strings`
    s=$(strings "$file_name")

    # Инициализация переменных для хранения самого длинного слова и его длины
    ref_word=''        # Слово с максимальной длиной
    max_len=0          # Максимальная длина слова

    # Перебираем все строки, найденные командой `strings`
    for i in $s; do
        len=${#i}       # Определяем длину текущей строки

        if [ $len -gt $max_len ]; then
            ref_word=$i       # Сохраняем текущее слово как самое длинное
            max_len=$len      # Обновляем максимальную длину
        fi
    done

    # Вывод результатов
    echo "Longest string: $ref_word"
    echo "Length: $max_len"

else
    # Сообщение, если файл недоступен для чтения
    echo "File NOT Readable/Non existing"
fi

# Финальный вывод
echo "##############################################"
echo " MAX LENGTH  is: $max_len"
echo " LONGEST word is: $ref_word"
