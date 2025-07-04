#!/bin/bash

# Путь к файлу с данными пользователей
FILE=/etc/passwd

# Ввод имени пользователя
read -p "Enter the name of the username: " user_name

# Поиск информации о пользователе
info=$(grep "^$user_name:" $FILE)

# Печать найденной строки
echo "$info"

# Сохраняем текущий IFS и устанавливаем новый
old_IFS=$IFS
IFS=:

# Проверка, найден ли пользователь
if [ -n "$info" ]; then

    # Чтение данных о пользователе
    read user pw uid gid full home shell <<< "$info"

    # Вывод данных
    echo "user is: $user"
    echo "pass is: $pw"
    echo "uid is: $uid"
    echo "gid is: $gid"
    echo "name is: $full"
    echo "home is: $home"
    echo "shell is: $shell"

else
    echo "User not Found"
fi

# Восстанавливаем оригинальный IFS
IFS=$old_IFS
