import asyncio
from app import asyncSessionLoader
from app.utils import measureExecutionTime
import app.crud
import datetime
from flask import Blueprint, jsonify
from flask_cors import cross_origin

views: Blueprint = Blueprint("views", __name__)

@views.get("/about")
async def about() -> dict:
    await asyncio.sleep(12)
    return {"about":"about"}

@views.route("/contact")
async def contact() -> dict:
    return {}

@views.route("/education")
async def education() -> dict:
    return {}

@views.route("/skills")
async def skills() -> dict:
    return {}

@views.route("/work-experience")
async def workExperience() -> dict:
    return {}

@views.route("/projects")
async def projects() -> dict:
    return {}

