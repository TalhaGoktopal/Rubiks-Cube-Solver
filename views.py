from flask import Blueprint, render_template
from cube import *

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("Home.html", name = "Talha")

@views.route("/solver")
def solver():
    return render_template("Solver.html", name = "Talha")

@views.route("/timer")
def timer():
    return render_template("Timer.html", name = "Talha")