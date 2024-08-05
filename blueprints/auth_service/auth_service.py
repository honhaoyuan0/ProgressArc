from flask import Blueprint, render_template, redirect, url_for

auth_bp= Blueprint("auth_bp", __name__,
                        template_folder = "templates",
                        static_folder= "static")

@auth_bp.route("/")
def index():
    return "Inside of auth_service endpoint !"

@auth_bp.route("/render")
def render():
    return render_template("/auth_service/render.html")

@auth_bp.route("/go_to_frontend")
def go_to_frontend():
    return redirect(url_for("frontend_bp.render"))

