from flask import Flask, flash, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
#db = SQL("sqlite:///finance.db")

# Dashboard
@app.route("/")
def dashboard():
    """Dashboard"""
    return render_template("dashboard.html")

# Sources
@app.route("/sources.html")
def sources():
    return render_template("sources.html")