from app import asyncSessionLoader
from app.utils import measureExecutionTime
import app.crud
import datetime
from flask import Blueprint
from flask_login import login_required, logout_user, current_user
from flask_cors import cross_origin

auth: Blueprint = Blueprint("auth", __name__)

@auth.route("/login")
@cross_origin()
async def login() -> str:
    return  {}

@auth.route("/verificate-user/<user>/<password>")
@cross_origin()
async def verificateUser(user: str, password: str):
    return {}

@login_required
@auth.route("/adminPage")
@cross_origin()
async def adminPage() -> str:
    return {}