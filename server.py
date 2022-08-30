from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/index/<int:num>')
def num(num):
    return render_template("num.html", num=num)



if __name__ == "__main__":
    app.run(debug=True)