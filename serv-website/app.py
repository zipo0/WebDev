from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, MultipleFileField
from mcstatus import JavaServer
import os
from werkzeug.utils import secure_filename

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Конфигурация приложения
app.config['SECRET_KEY'] = 'your_secret_key'  # Замените на свой секретный ключ
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Ограничение на 16MB

# Создаем экземпляр SQLAlchemy и привязываем его к приложению
db = SQLAlchemy(app)

# Создаем объект для миграции базы данных
migrate = Migrate(app, db)

# Определение модели News
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    publication_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    author = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(10), default='published')
    images = db.relationship('NewsImage', backref='news', lazy=True, cascade="all, delete-orphan")

# Определение модели NewsImage
class NewsImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'), nullable=False)

# Определение формы NewsForm
class NewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    images = MultipleFileField('Images', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Submit')

# Маршрут для удаления новости
@app.route('/delete_news/<int:news_id>', methods=['POST'])
def delete_news(news_id):
    news_item = News.query.get(news_id)  # Найти новость по ID
    if news_item:
        password = request.form.get('delete_password')
        if password == 'Leva2015':  # Замените на свой пароль
            db.session.delete(news_item)  # Удалить новость из базы данных
            db.session.commit()  # Сохранить изменения
            flash('News deleted successfully!', 'success')
        else:
            flash('Incorrect password. News was not deleted.', 'error')
    else:
        flash('News not found!', 'danger')
    return redirect(url_for('admin'))  # Перенаправить обратно в админ-панель

# Главная страница
@app.route('/home')
def home():
    mconline = getOnline()
    return render_template('index.html', online=mconline)

# Страница новостей
@app.route('/news')
def news():
    mconline = getOnline()
    news_items = News.query.order_by(News.publication_date.desc()).all()  # Fetch all news items sorted by publication date
    return render_template('news.html', news_items=news_items, online=mconline)

# Страница администрирования
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = NewsForm()
    
    if form.validate_on_submit():
        password = request.form.get('password')
        if password == 'Leva2015':  # Use your actual password
            # Создаем новую запись о новости
            new_news = News(
                title=form.title.data,
                content=form.content.data,
                author='Admin'
            )
            db.session.add(new_news)
            db.session.commit()

            # Сохраняем загружаемые изображения
            for image_file in form.images.data:
                if image_file:
                    filename = secure_filename(image_file.filename)
                    image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    
                    # Добавляем запись об изображении в базу данных
                    news_image = NewsImage(filename=filename, news_id=new_news.id)
                    db.session.add(news_image)

            db.session.commit()
            flash('News added successfully!', 'success')
            return redirect(url_for('admin'))
        else:
            flash('Incorrect password. Please try again.', 'danger')

    news_items = News.query.order_by(News.publication_date.desc()).all()
    return render_template('admin.html', form=form, news_items=news_items)

# Страница онлайн карты
@app.route('/onlinemap')
def onlinemap():
    # Здесь логика для отображения онлайн карты
    mconline = getOnline()
    return render_template('map.html', online=mconline)

# Страница магазина
@app.route('/shop')
def shop():
    return render_template('shop.html')

# Функция для получения информации о количестве игроков онлайн на сервере
def getOnline():
    server = JavaServer.lookup("mc.lunvex.online")
    status = server.status()
    return status.players.online

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
