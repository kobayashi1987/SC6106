#blockchain application

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET","POST"])
def main():
    return(render_template("main.html"))


@app.route("/transferMoney", methods=["GET","POST"])
def transferMoney():
    return(render_template("transferMoney.html"))


@app.route("/storeMoney", methods=["GET","POST"])
def storeMoney():
    return(render_template("storeMoney.html"))

@app.route("/invoice", methods=["GET","POST"])
def invoice():
    return(render_template("invoice.html"))


if __name__ == "__main__":
    app.run()


