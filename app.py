from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def mainpage():
  return render_template("main.html")


@app.route('/form')
def form():
    return render_template("form.html")

if __name__ == "__main__":
  app.run(debug=True) 