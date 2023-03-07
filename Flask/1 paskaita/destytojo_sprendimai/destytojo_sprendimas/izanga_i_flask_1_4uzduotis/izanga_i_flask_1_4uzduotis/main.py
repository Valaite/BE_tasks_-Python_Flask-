#4 užduotis
#Sukurti programą, kuri leistų įvesti metus ir 
#paspaudus patvirtinimo mygtuką parodytų, ar jie yra keliamieji.

from flask import Flask, render_template, request
import calendar

app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def dashboard():
#     if request.method == "POST":
#         year = request.form["year"]
#         return render_template("postyear_if.html", year=int(year), calendar=calendar)
#     else:
#         return render_template("getyear.html")

@app.route("/", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        year = request.form["year"]
        
        if calendar.isleap(int(year)):
            answer = "is leap year"
        else:
            answer = "Not lep year"
        
        return render_template("postyear_notif.html", answer=answer)
    else:
        return render_template("getyear.html")

# @app.route("/", methods=["GET", "POST"])
# def dashboard():
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
        

if __name__ == "__main__":
    app.run()
