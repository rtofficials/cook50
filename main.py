from flask import Flask, request, render_template
import sqlite3
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
        rtype =  request.form["r_type"]
        prep_time =  request.form["prep_time"]
        main_ingredients = request.form["main_ingredients"]
        last_made =  request.form["last_made"]
        details_link = request.form["details_link"]
        params = (rname, rating, difficulty_level, rtype, prep_time, main_ingredients, last_made, details_link)
        con = sqlite3.connect("cook50.db")
        c = con.cursor();
        try:
            c.execute("INSERT INTO recipes VALUES(?, ?, ?, ?, ?, ?, ?, ?)", params)
            con.commit()
            con.close()
            return "Recipe Added.\n"
        except sqlite3.Error as e:
            print("something went wrong :  ", e)
            return "Uh oh! Recipe not added. Retry adding " + rname + "again.\n"
    return render_template("add_recipe.html")

@app.route("/recipe_list")
def recipe_list():
    con = sqlite3.connect("cook50.db")
    print("established")
    c = con.cursor();
    print("cursor created")
    c.execute("SELECT rowid, * FROM RECIPES;")
    rows = c.fetchall()
    return render_template("recipe_list.html",  rows=rows)

@app.route("/timer")

def timer():
    s=50;
    m=59;
    h=0;
    while(True):
        print('%d : %d  : %d' %(h, m, s))
        time.sleep(1)
        s += 1;
        if s==60:
            s=0;
            m+=1
        if m==60:
            m=0
            h =+ 1;
        os.system('clear')
    return render_template("timer.html", h=h, m=m,s=s)

if __name__ == '__main__':
    app.run(debug=True)
