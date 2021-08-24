from flask import Flask, request, render_template
import sqlite3
import os, time, keyboard, sys
app = Flask(__name__)

def connection():
    con = sqlite3.connect("cook50.db")
    c = con.cursor();

@app.route("/")
def home():
    return render_template("home.html");

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method=="POST":
        rname = request.form["rname"]
        rating = request.form["rating"]
        difficulty_level = request.form["difficulty_level"]
        r_type =  request.form["r_type"]
        prep_time =  request.form["prep_time"]
        main_ingredients = request.form["main_ingredients"]
        last_made =  request.form["last_made"]
        details_link = request.form["details_link"]
        params = (rname, rating, difficulty_level, r_type, prep_time, main_ingredients, last_made, details_link)
        print(params)
        con = sqlite3.connect("cook50.db")
        print("add : established")
        c = con.cursor();
        print("add : cursor created")
        try:
            c.execute("INSERT INTO recipes VALUES(?, ?, ?, ?, ?, ?, ?, ?)", params)
            con.commit()
            con.close()
            return "Recipe Added.\n"
        except sqlite3.Error as e:
            print("something went wrong :  ", e)
            return "Uh oh! Recipe not added. Retry adding " + rname + " again.\n"
    return render_template("add_recipe.html")

@app.route("/recipe_list")
def recipe_list():
    con = sqlite3.connect("cook50.db")
    print("list : established")
    c = con.cursor();
    print("list : cursor created")
    c.execute("SELECT rowid, * FROM RECIPES ORDER BY rname;")
    rows = c.fetchall()
    return render_template("recipe_list.html",  rows=rows)

@app.route("/timer")
def timer():
    print ("Timer will be added soon. WIP")
    return render_template('timer.html')

if __name__ == '__main__':
    app.run(debug=True)
