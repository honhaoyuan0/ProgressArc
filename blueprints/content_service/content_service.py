from flask import Blueprint, render_template, redirect, url_for

content_bp = Blueprint("content_bp", __name__, template_folder="templates", static_folder="static")

@content_bp.route("/")
def index():
    return "Inside of Content_service endpoint !"

@content_bp.route("/render")
def render():
    return render_template("content_service/render.html")

@content_bp.route("/go_to_frontend")
def go_to_frontend():
    return redirect(url_for("frontend_bp.render"))