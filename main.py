
# Домашняя работа на 23.07.2023

from flask import Flask, render_template, request

# Flask - класс для создания приложения

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': '/'},
    {'name': 'О сайте', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contacts'},
]

@app.route('/')  # чтобы Flask распознал путь к странице пишем декоратор
def index():   # Это функция-обработчик
    return render_template("index.html", title='Ввод параметров транзакции', menu=menu)

# Время 01:20:00 Лекция 49
# Второй обработчик (# Время 01:06:45 Лекция 49)
@app.route('/about')
def about():
    return render_template("about.html", menu=menu)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        return render_template("index.html", title='Главная', menu=menu)

    return render_template("contacts.html", title='Обратная связь', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)

