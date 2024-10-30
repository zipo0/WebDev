from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect, url_for, flash, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Замените на свой секретный ключ
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    publication_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    author = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(10), default='published')

class NewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')

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

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/news')
def news():
    news_items = News.query.order_by(News.publication_date.desc()).all()  # Fetch all news items sorted by publication date
    return render_template('news.html', news_items=news_items)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = NewsForm()
    
    # Handle the form submission for adding news
    if form.validate_on_submit():
        password = request.form.get('password')
        if password == 'Leva2015':  # Use your actual password
            new_news = News(title=form.title.data, content=form.content.data, author='Admin')
            db.session.add(new_news)
            db.session.commit()
            flash('News added successfully!', 'success')
            return redirect(url_for('admin'))
        else:
            flash('Incorrect password. Please try again.', 'danger')

    # Fetch all news items sorted by publication date
    news_items = News.query.order_by(News.publication_date.desc()).all()
    return render_template('admin.html', form=form, news_items=news_items)

@app.route('/onlinemap')
def onlinemap():
    # Здесь логика для отображения онлайн карты
    return render_template('map.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')




if __name__ == '__main__':
    app.run(debug=True)