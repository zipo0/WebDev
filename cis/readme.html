<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Инструкция установки системы</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      background-color: #f4f4f4;
      margin: 20px;
    }
    h1 {
      color: #1e3c72;
      text-align: center;
    }
    h2 {
      color: #1e3c72;
      margin-top: 30px;
    }
    h3.note {
      color: red;
    }
    pre {
      background: #eaeaea;
      padding: 10px;
      border-radius: 4px;
      overflow-x: auto;
    }
    code {
      font-family: Consolas, monospace;
    }
    ol {
      margin-left: 20px;
    }
    li {
      margin-bottom: 20px;
    }
  </style>
</head>
<body>
  <h1>Инструкция установки системы</h1>

  <ol>
    <li>
      <strong>Клонирование репозитория:</strong>
      <p>Клонируйте репозиторий и перейдите в каталог проекта:</p>
      <pre><code>git clone &lt;URL_репозитория&gt; cis_reservation_system
cd cis_reservation_system</code></pre>
    </li>
    <li>
      <strong>Создание и активация виртуального окружения:</strong>
      <p>Создайте виртуальное окружение:</p>
      <pre><code>python -m venv venv</code></pre>
      <p>Активируйте виртуальное окружение:</p>
      <pre><code>
# Для Windows:
venv\Scripts\activate

# Для Linux/Mac:
source venv/bin/activate
      </code></pre>
    </li>
    <li>
      <strong>Установка зависимостей:</strong>
      <p>Убедитесь, что в корне проекта есть файл <code>requirements.txt</code>. Если его нет, создайте его командой:</p>
      <pre><code>pip freeze > requirements.txt</code></pre>
      <p>Затем установите зависимости:</p>
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>
      <strong>Настройка базы данных (PostgreSQL):</strong>
      <p>Настройте базу данных и пользователя. Например, в PostgreSQL выполните следующие команды (запустите psql от имени пользователя postgres):</p>
      <pre><code>CREATE DATABASE reservation_db;
CREATE USER myuser WITH PASSWORD 'mypassword';
ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE reservation_db TO myuser;
\q</code></pre>
      <p>Обновите раздел <code>DATABASES</code> в файле <code>settings.py</code>:</p>
      <pre><code>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'reservation_db',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
      </code></pre>
    </li>
    <li>
      <strong>Применение миграций, создание суперпользователя и сбор статики:</strong>
      <pre><code>python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic</code></pre>
    </li>
    <li>
      <strong>Создание записей для компьютеров (Shelves):</strong>
      <p>Для создания 20 записей для каждого этажа (например, для 2 и 3 этажей) используйте management command. Убедитесь, что у вас есть структура:</p>
      <pre><code>booking/
  management/
    __init__.py
    commands/
      __init__.py
      create_shelves.py</code></pre>
      <p>Пример кода в файле <code>create_shelves.py</code>:</p>
      <pre><code>from django.core.management.base import BaseCommand
from booking.models import Shelf

class Command(BaseCommand):
    help = 'Creates 20 shelves (laptops) for each floor (2 and 3)'

    def handle(self, *args, **options):
        floors = [2, 3]
        total_created = 0
        for floor in floors:
            for number in range(1, 21):  # от 1 до 20
                shelf, created = Shelf.objects.get_or_create(floor=floor, number=number)
                if created:
                    total_created += 1
                    self.stdout.write(f"Created shelf: Floor {floor} - N {number}")
        self.stdout.write(self.style.SUCCESS(f"Total shelves created: {total_created}"))
</code></pre>
      <p>Запустите команду:</p>
      <pre><code>python manage.py create_shelves</code></pre>
    </li>
    <li>
      <strong>Запуск системы:</strong>
      <p>Для проверки работы сайта запустите сервер разработки:</p>
      <pre><code>python manage.py runserver</code></pre>
    </li>
    <li>
      <strong>Автоматическое удаление просроченных бронирований через Windows Task Scheduler:</strong>
      <p>Настройте Windows Task Scheduler для периодического запуска команды, которая удаляет просроченные бронирования. Пример команды (каждые 5 минут):</p>
      <pre><code>
C:\Users\Admin\cis\venv\Scripts\python.exe C:\Path\To\Your\Project\manage.py clear_expired_bookings >> C:\Path\To\Your\Project\cron.log 2>&1
      </code></pre>
      <p>Настройте задачу через Windows Task Scheduler, следуя стандартным шагам.</p>
    </li>
  </ol>

  <h3 class="note">(Опционально) Продакшн-развёртывание</h3>
  <p class="note">Настройте Gunicorn и Nginx для продакшн-развёртывания, используя systemd и конфигурацию Nginx.</p>

</body>
</html>
