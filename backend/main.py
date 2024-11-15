from app import createApp
from flask import Flask, url_for, redirect
import subprocess

app: Flask = createApp()

@app.route('/')
async def index():
    return redirect(url_for("views.about"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)