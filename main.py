from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    title = "Sign up"
    return render_template("index.html", title=title)





if __name__ == "__main__":
    app.run(debug=True)