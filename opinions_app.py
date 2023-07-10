from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Создаётся экземпляр класса SQLAlchemy и передаётся 
# в качестве параметра экземпляр приложения Flask
# db = SQLAlchemy(app)

# Второй шаг — сообщить SQLAlchemy, где находится база данных, и как её подключить. Это делается по шаблону:
# dialect+driver://username:password@host:port/database 

# dialect — тип базы данных.
# driver — драйвер для соединения с базой данных.
# username и password — имя пользователя и пароль для подключения базы данных.
# host — местоположение сервера базы данных.
# port — порт сервера базы данных.
# database — имя базы данных.
# Формат подключения SQLite:

# для абсолютного адреса в ОС Windows
# sqlite:///C:\dev\what_to_watch\db.sqlite3

# для абсолютного адреса в ОС Unix/Mac
# sqlite:////username/dev/what_to_watch/db.sqlite3

# для относительного адреса в ОС Unix/Mac/Windows
# sqlite:///db.sqlite3 

# Подключается БД SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# Задаётся конкретное значение для конфигурационного ключа
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index_view():

    # Это ключи конфигурации, которые используются по умолчанию. 
    # Их значения можно запрашивать и менять, что вы обязательно сделаете в рамках этого курса. 
    # Можно добавлять и собственные ключи, эта возможность вам тоже пригодится в ближайшее время. 
    # print(app.config)
    return 'Совсем скоро тут будет случайное мнение о фильме!'

if __name__ == '__main__':
    app.run()