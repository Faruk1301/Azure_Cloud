from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Azure! This is a simple Python script running with Flask. From Bangladesh, England, and GER."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

