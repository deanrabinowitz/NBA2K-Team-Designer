import sys
from flask import Flask
sys.path.append("..")
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world"

if __name__ == "__main__":
    app.run()