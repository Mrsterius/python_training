from flask import Flask

app = Flask("chacha")

@app.route("/home/")
def hello():
    return "something"

app.run(port=5000)