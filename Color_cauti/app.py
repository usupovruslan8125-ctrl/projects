from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html", title="Миссия Колонизация Марса")


@app.route("/table/<gender>/<int:age>")
def table(gender, age):
    if gender == "male":
        if age < 21:
            wall_color = "#aec6cf"
        else:
            wall_color = "#0000ff"
    else:
        if age < 21:
            wall_color = "#f4c2c2"
        else:
            wall_color = "#ff0000"
    if age < 21:
        image = "martian_kid.jpg"
    else:
        image = "martian_adult.jpg"
    return render_template("table.html", wall_color=wall_color, image=image)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
