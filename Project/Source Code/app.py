from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='./template')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/story")
def story():
    return render_template("story.html")

# run server
if __name__ == "__main__":
    app.run(debug=True)