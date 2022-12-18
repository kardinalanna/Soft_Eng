### Software-Engineering
# Telegram-bot для парсинга поисковой выдачи YouTube
[![master](https://github.com/kardinalanna/Software-Engineering/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/kardinalanna/Software-Engineering/actions/workflows/test.yml) main

[![master](https://github.com/kardinalanna/Software-Engineering/actions/workflows/test.yml/badge.svg?branch=develop)](https://github.com/kardinalanna/Software-Engineering/actions/workflows/test.yml) develop

С помощью этого бота можно производить поиск в youtube,используя строку ввода сообщения, и сразу делиться ссылкой на видио.

### Запуск 
Используя Docker:
   1. Запустите терминал в папке проекта.
   2. Введите следующие команды:
    
    docker  build . -t ytparser 
    docker run ytparser

Без докера:
 1. Склонируйте репозиторий себе на комьютер: git clone https://github.com/kardinalanna/Software-Engineering.git
 2. Создайте виртуальное окружение в папке с проектом и установите нужные библиотеки при помощи команды в терминале: pip install -r requirements.txt
 3. Запустите python main файл командой: python main.py
 
 ### Пример работы
После запуска бота обратитесь к нему @parseYT_bot и напишите запрос. Выберете подходящее видио в появившемся окне.


 ![alt text](https://github.com/kardinalanna/Software-Engineering/blob/main/exp_img.PNG?raw=true)

