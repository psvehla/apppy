from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world.\n"

@app.route("/version")
def version():
    return "Helloworld 1.0\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
