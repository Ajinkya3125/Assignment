from flask import Flask,render_template,redirect,request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Admin@123'
app.config['MYSQL_DB'] = 'todoapidb'

mysql = MySQL(app)

@app.route("/")
def get_todos():
    con = mysql.connection.cursor()
    con.execute("select * from todoapitb")
    todos = con.fetchall()
    print(todos)
    # return str(todos)
    return render_template("index.html",todos=todos)

@app.route("/delete/<int:todoId>")
def delete_todo(todoId):
    con = mysql.connection.cursor()
    con.execute(f"delete from todoapitb where todoId = {todoId}")
    con.connection.commit()
    return redirect("/")

@app.route("/add",methods=["POST"])
def add_todo():
    # print(request.form['title'])
    # print(request.form['desc'])
    title = request.form['title']
    desc = request.form['desc']
    con = mysql.connection.cursor()
    con.execute(f"insert into todoapitb(todoTitle,todoDescription) values('{title}','{desc}')")
    con.connection.commit()
    return redirect("/")

@app.route("/edit/<int:todoId>",methods=["GET","POST"])
def edit_todo(todoId):
    con = mysql.connection.cursor()
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        con.execute(f"update todoapitb set todoTitle = '{title}', todoDescription = '{desc}' where todoId = {todoId}")
        con.connection.commit()
        return redirect("/")
    else:
        con.execute(f"select * from todoapitb where todoId = {todoId}")
        data = con.fetchone()
        print(data)
        return render_template("index.html",edit_todo=data)

# @app.route('/user/<name>')
# def user(name):
#     return f"hello,{name}!"

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)