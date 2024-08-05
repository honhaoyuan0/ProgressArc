from flask import Blueprint, render_template

frontend_bp = Blueprint("frontend_bp", __name__, template_folder="templates", static_folder="static")

@frontend_bp.route("/")
def index():
    return "Inside of Frontend !"

@frontend_bp.route("/render")
def render():
    return render_template("frontend/render.html")