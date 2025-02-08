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
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    h1 {
      text-align: center;
      margin-bottom: 30px;
      color: #1e3c72;
    }
    p {
      font-size: 1.1rem;
      margin-bottom: 15px;
    }
    strong {
      color: #1e3c72;
    }
    .optional {
      color: #a00;
      font-style: italic;
      margin-top: 20px;
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
  </style>
</head>
<body>
  <div class="container">
    <h1>Инструкция</h1>
    <p><strong>1.</strong> Клонируйте репозиторий и перейдите в каталог проекта.</p>
    <p><strong>2.</strong> Создайте и активируйте виртуальное окружение.</p>
    <p><strong>3.</strong> Установите зависимости через <code>pip install -r requirements.txt</code>.</p>
    <p><strong>4.</strong> Настройте базу данных (PostgreSQL) и обновите <code>DATABASES</code> в <code>settings.py</code>.</p>
    <p><strong>5.</strong> Запустите миграции (<code>python manage.py migrate</code>), создайте суперпользователя (<code>python manage.py createsuperuser</code>) и соберите статические файлы (<code>python manage.py collectstatic</code>).</p>
    <p><strong>6.</strong> Создайте модель (SPB: <code>python manage.py create_shelves</code>).</p>
    <p><strong>7.</strong> Запустите сервер разработки для проверки работы сайта (<code>python manage.py runserver [ip]</code>).</p>
    <p class="optional">(Опционально) Настройте Gunicorn и Nginx для продакшн-развёртывания, используя systemd и конфигурацию Nginx.</p>
  </div>
</body>
</html>
