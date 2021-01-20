from flask import Flask,render_template,url_for

app = Flask(__name__)


@app.route("/home")
def me():
    return "hello work"

@app.route("/")
def index():
    return render_template('index.html')



app.run()
