from flask import Blueprint, render_template, redirect, url_for

user_bp = Blueprint("user_bp", __name__, template_folder="templates", static_folder="static")

@user_bp.route("/")
def index():
    return "Inside of User_Service endpoint !"

@user_bp.route("/render")
def render():
    return render_template("/user_service/render.html")

@user_bp.route("/go_to_frontend")
def go_to_frontend():
    return redirect(url_for("frontend_bp.render"))