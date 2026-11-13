#blockchain application

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return("Welcome to Blockchain application")

if __name__ == "__main__":
    app.run()


