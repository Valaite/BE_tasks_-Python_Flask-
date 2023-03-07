from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    html_data = "Pagrindinis puslapis"
    return render_template("index.html", data=html_data)


@app.route("/<string:name>")
def name_print(name):
    return render_template("name_print.html", data=name)


@app.route("/keliamieji")
def show_leap():
    years_data = []
    for year in range(1900, 2101):
        years_data.append(year)
    return render_template("leap_years.html", years=years_data)


@app.route("/ar-keliamieji", methods=["GET", "POST"])
def is_leap():
    leap_year = False
    year = None

    if request.method == "POST":
        try:
            year = int(request.form['metai'])
            if year % 4 == 0:
                if year % 100 == 0 and year % 400 != 0:
                    leap_year = False
                else:
                    leap_year = True
            else:
                leap_year = False
        except (TypeError, ValueError):
            leap_year = False
    return render_template("leap_year.html", leap_year=leap_year, metai=year)


if __name__ == "__main__":
    app.run(debug=True)
