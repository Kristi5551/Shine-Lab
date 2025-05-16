from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/booking", methods=["GET", "POST"])
def booking():
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
    if request.method == "POST":
        name = request.form["name"]
        review = request.form["review"]
        print(f"Отзыв от {name}: {review}")
    return render_template("feedback.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "True") == "True"
    app.run(host="0.0.0.0", port=port, debug=debug)