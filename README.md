# Сеть по продаже электроники

# Поставленные задачи:

1. Создать веб-приложение с API-интерфейсом и админ-панелью.  
2. Создайте базу данных, используя миграции Django.

Приложение выполнено на Django REST framework

# Стек:  
Python 3.8+  
Django 3+  
DRF 3.10+  
PostgreSQL 10+  

# Для запуска проекта необходимо сделать следующее:  
1. Git clone репозитория:  
https://github.com/Kr4b1x/electronics_store_by_skypro.git  
2. Установить виртуальное окружение venv:  
python3 -m venv venv для MacOS и Linux систем  
python -m venv venv для windows  
3. Активировать виртуальное окружение:  
source venv/bin/activate для MasOs и Linux систем  
venv\Scripts\activate.bat для windows  
4. Установить файл с зависимостями:  
pip install -r requirements.txt  
5. Создать базу данных в PgAdmin, либо через терминал:  
Необходимо дать название в файле settings.py в каталоге 'config' в константе (словаре) 'DATABASES'  
6. Создать в корне проекта файл .env и заполнить его данными из файла .env.example

7. Для запуска проекта использовать команду:  
python manage.py ruserver

# Так же для удобства, в проекте присутствует файл csu для быстрого создания суперпользователя с помощью следующей команды:  
python manage.py csu
