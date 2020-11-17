from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///login.db'
app.secret_key = "6@sttdklmt!ma2#"

db = SQLAlchemy(app)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(20), nullable=False) 
    email = db.Column(db.String(50), nullable=False) 
    password = db.Column(db.String(20), nullable=False) 

    def __repr__(self):
        return (f"name:{self.username}, password:{self.password}")


@app.route("/")
@app.route("/login", methods=["POST", "GET"])
def login():
    title = "SIGN UP"
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        new_members = Login(username=name, email=email, password=password)
        try:
            #add new members to database
            db.session.add(new_members)
            #commit new mebers to database
            db.session.commit()
        except:
            return "Problem occured while saving your info"
        
    else:
        return render_template("index.html", title=title)

@app.route("/home", methods=["POST", "GET"])
def home():
    title = "Welcome"
    members = Login.query.all()
    return render_template("home.html", members=members, title=title)


if __name__ == "__main__":
    app.run(debug=True)