<h1>Итоговая инструкция</h1>
<p>1. Клонируйте репозиторий и перейдите в каталог проекта.</p>
<p>2. Создайте и активируйте виртуальное окружение.</p>
<p>3. Установите зависимости через pip install -r requirements.txt.</p>
<p>4. Настройте базу данных (PostgreSQL) и обновите DATABASES в settings.py.</p>
<p>5. Запустите миграции (python manage.py migrate), создайте суперпользователя (python manage.py createsuperuser) и соберите статические файлы (python manage.py collectstatic).</p>
<p>6. Создайте модель (SPB: python manage.py create_shelves)</p>
<p>7. Запустите сервер разработки для проверки работы сайта (python manage.py runserver).</p>
<p><r>(Опционально) Настройте Gunicorn и Nginx для продакшн-развёртывания, используя systemd и конфигурацию Nginx.</r><</p>