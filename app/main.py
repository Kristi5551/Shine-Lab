from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    """
    Главная страница сайта.

    Возвращает:
        Рендер шаблона 'index.html' — главной страницы сайта.
    """
    return render_template("index.html")


@app.route("/booking", methods=["GET", "POST"])
def booking():
    """
    Страница записи на услугу.

    GET:
        Отображает пустую форму для записи.
    POST:
        Получает данные из формы:
            - name (имя клиента)
            - phone (номер телефона)
            - date (дата записи)
            - time (время записи)
            - service (услуга)
        Выводит информацию о записи в консоль.
        Возвращает страницу 'booking.html' с заполненными данными.

    Возвращает:
        Рендер шаблона 'booking.html' с параметрами формы (при POST) или пустой формой (при GET).
    """
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        date = request.form["date"]
        time = request.form["time"]
        service = request.form["service"]
        print(f"Запись: {name}, {phone}, {date}, {time}, {service}")
        return render_template("booking.html", name=name, phone=phone, date=date, time=time, service=service)
    return render_template("booking.html")


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    """
    Страница отзывов.

    GET:
        Отображает пустую форму для отзыва.
    POST:
        Получает данные из формы:
            - name (имя оставившего отзыв)
            - review (текст отзыва)
        Выводит отзыв в консоль.

    Возвращает:
        Рендер шаблона 'feedback.html'.
    """
    if request.method == "POST":
        name = request.form["name"]
        review = request.form["review"]
        print(f"Отзыв от {name}: {review}")
    return render_template("feedback.html")


if __name__ == "__main__":
    """
    Точка входа в приложение.

    Получает порт и режим отладки из переменных окружения:
        - PORT (по умолчанию 5000)
        - DEBUG (по умолчанию True)

    Запускает Flask-приложение на хосте 0.0.0.0 с заданным портом и режимом отладки.
    """
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "True") == "True"
    app.run(host="0.0.0.0", port=port, debug=debug)
