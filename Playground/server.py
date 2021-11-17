from os import times
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", times=3)

@app.route('/play/<int:x>')
def multiplier(x):
    return render_template("index.html",times=x)

@app.route('/play/<int:x>/<color>')
def multiplier_color(x,color):
    return render_template("index.html",times=x, color=color)

if __name__=="__main__":
    app.run(debug=True)