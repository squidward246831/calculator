import os
from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def source():
    render_template("index12.html")