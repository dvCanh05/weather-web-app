from flask import Flask, render_template, request
import requests
import json


url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=5651c5511e1bea3dfaa97f4575fd1e91"

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form.get("city")
        r = requests.get(url.format(city_name))
        
        if r.status_code == 200:
            json_object = r.json()

            temperature = int(json_object["main"]["temp"] - 272.15)
            humidity = int(json_object["main"]["humidity"])
            pressure = int(json_object["main"]["pressure"])
            wind = int(json_object["wind"]["speed"])
            condition = json_object["weather"][0]["main"]
            desc = json_object["weather"][0]["description"]

            return render_template(
                "home.html",
                temperature=temperature,
                pressure=pressure,
                humidity=humidity,
                city_name=city_name,
                condition=condition,
                wind=wind,
                desc=desc,
            )
        else:
            return render_template("home.html")
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
