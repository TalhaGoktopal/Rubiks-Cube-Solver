from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/solver")
def solver():
    return render_template("index.html", name = "Talha")

@views.route("/timer")
def timer():
    return render_template("index.html", name = "Talha")