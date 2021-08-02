from flask import Flask, request
import sqlite3

app = Flask(__name__)
def connection():
    con = sqlite3.connect("cook50.db")
    c = con.cursor();

@app.route('/')
def home():
    return "on home page";

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method=="POST":
        rname = request.form["rname"]
        rating = request.form["rating"]
        difficulty_level = request.form["difficulty_level"]
        rtype =  request.form["type"]
        prep_time =  request.form["prep_time"]
        main_ingredients = request.form["main_ingredients"]
        last_made =  request.form["last_made"]
        details_link = request.form["details_link"]
        params = (rname, rating, difficulty_level, rtype, prep_time, main_ingredients, last_made, details_link)
        try:
            c.execute("INSERT INTO recipes VALUES( ?, ?, ?, ?, ?, ?, ?, ?)", params)
            con.commit()
            con.close()
            return "Recipe Added.\n"
        except sqlite3.Error as e:
            print("something went wrong :  ", e)
            return False

@app.route("/recipe_list")
def recipe_list():
    con = sqlite3.connect("cook50.db")
    print("established")
    c = con.cursor();
    print("cursor created")
    result = c.execute("select * from recipes")
    print(result)
    return render_template("recipe_list.html",  rows=c.fetchall())

if __name__ == '__main__':
    app.run(debug=True)
