from flask import Flask, flash, redirect, render_template, request
import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


def upsertStats(dbconn, schoolname, date, testnum, positivenum):
    dbconn.cursor().execute("INSERT OR REPLACE INTO university_covid_stats values (?, ?, ?, ?)", (schoolname, date, testnum, positivenum))
    dbconn.commit()

def main():
    con = sqlite3.connect('covid_stats.db')
    cur = con.cursor()

    #upsertStats(con, "a", "2021/11/28", 200, 22)

    for row in cur.execute('SELECT * FROM university_covid_stats ORDER BY university_name, date'):
            print(row)

    con.close()


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


main()