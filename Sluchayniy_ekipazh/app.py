from flask import Flask, render_template
import json
import random


app = Flask(__name__)


@app.route("/member")
def member():
    with open("templates/crew.json", "r", encoding="utf-8") as f:
        crew = json.load(f)
    return render_template("member.html", title="Случайный член экипажа", crew=crew)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")