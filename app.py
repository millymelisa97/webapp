from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home_page():
    return "Helo World"

@app.route("/greeting")
def display():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()