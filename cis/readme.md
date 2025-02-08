<h1>Инструкция</h1>
<p><b>1.</b> Клонируйте репозиторий и перейдите в каталог проекта.</p>
<p><b>2.</b> Создайте и активируйте виртуальное окружение.</p>
<p><b>3.</b> Установите зависимости через pip install -r requirements.txt.</p>
<p><b>4.</b> Настройте базу данных (PostgreSQL) и обновите DATABASES в settings.py.</p>
<p><b>5.</b> Запустите миграции (python manage.py migrate), создайте суперпользователя (python manage.py createsuperuser) и соберите статические файлы (python manage.py collectstatic).</p>
<p><b>6.</b> Создайте модель (SPB: python manage.py create_shelves)</p>
<p><b>7.</b> Запустите сервер разработки для проверки работы сайта (python manage.py runserver [ip]).</p>
<p><r>(Опционально) Настройте Gunicorn и Nginx для продакшн-развёртывания, используя systemd и конфигурацию Nginx.</r><</p>