<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Инструкция установки системы</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f8f8f8;
      margin: 0;
      padding: 20px;
      line-height: 1.6;
      color: #333;
    }
    .container {
      max-width: 800px;
      margin: auto;
      background: #fff;
      padding: 30px 40px;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    h1 {
      color: #1e3c72;
      text-align: center;
      margin-bottom: 30px;
    }
    p {
      font-size: 1.1rem;
      margin-bottom: 15px;
    }
    b {
      color: #1e3c72;
    }
    /* Если тег <r> используется для выделения опциональной информации */
    r {
      color: #a00;
      font-style: italic;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Инструкция</h1>
    <p><b>1.</b> Клонируйте репозиторий и перейдите в каталог проекта.</p>
    <p><b>2.</b> Создайте и активируйте виртуальное окружение.</p>
    <p><b>3.</b> Установите зависимости через pip install -r requirements.txt.</p>
    <p><b>4.</b> Настройте базу данных (PostgreSQL) и обновите DATABASES в settings.py.</p>
    <p><b>5.</b> Запустите миграции (python manage.py migrate), создайте суперпользователя (python manage.py createsuperuser) и соберите статические файлы (python manage.py collectstatic).</p>
    <p><b>6.</b> Создайте модель (SPB: python manage.py create_shelves)</p>
    <p><b>7.</b> Запустите сервер разработки для проверки работы сайта (python manage.py runserver [ip]).</p>
    <p><r>(Опционально) Настройте Gunicorn и Nginx для продакшн-развёртывания, используя systemd и конфигурацию Nginx.</r><</p>
  </div>
</body>
</html>
