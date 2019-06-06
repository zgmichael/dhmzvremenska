# glavni program

import requests

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():

    grad = "Zagreb"

    unit = "metric"

    apikey = "a584720c43c130d020ae58d96440565e"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("index.html", data=data.json())


@app.route("/Osijek", methods=["GET"])
def osijek():

    grad = "Osijek"

    unit = "metric"

    apikey = "a584720c43c130d020ae58d96440565e"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("Osijek.html", data=data.json())


@app.route("/Rijeka", methods=["GET"])
def rijeka():

    grad = "Rijeka"

    unit = "metric"

    apikey = "a584720c43c130d020ae58d96440565e"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("Rijeka.html", data=data.json())


@app.route("/Split", methods=["GET"])
def split():

    grad = "Split"

    unit = "metric"

    apikey = "a584720c43c130d020ae58d96440565e"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("Split.html", data=data.json())







if __name__ == "__main__":
    app.run()

