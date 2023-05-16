from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    if request.method === "POST":
        name = request.args.get("name", "world")
        return render_template("index.html", name=name)
