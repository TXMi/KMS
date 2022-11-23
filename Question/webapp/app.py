from flask import Flask
from flask import render_template, request

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    msg = ""

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        print(password)

        file = open("password.txt")
        for line in file:
            if password in line:
                msg = "Please choose a more secured password"
                print(msg)
                return render_template("index.html", msg=msg)
        msg = "Password is secured enough"
        print("Password is secured enough")
        return render_template("home.html")

    return render_template("index.html", msg=msg)

@app.route("/home")
def home():
    return render_template("home.html")

if __name__=="__main__":
    app.run()