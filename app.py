from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Azure & GitHub Actions! i edit this file 5 times "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
