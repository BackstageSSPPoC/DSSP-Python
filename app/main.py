from flask import Flask
from calculator import add, divide

app = Flask(__name__)

@app.route("/")
def home():
    try:
        division_result = divide(10, 0)
    except ValueError as e:
        division_result = str(e)

    return {
        "message": "Application Started",
        "addition_result": add(10, 5),
        "division_result": division_result
    }

if __name__ == "__main__":
    print("[LOG] Flask Server Started")
    app.run(host="0.0.0.0", port=5000)
