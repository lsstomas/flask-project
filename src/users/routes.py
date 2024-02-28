from . import user_bp
from flask import render_template, redirect, url_for


@user_bp.route("/login")
def login():
    return "Login"
