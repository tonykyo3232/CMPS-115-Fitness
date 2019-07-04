from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return "hello, world!"

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        port = int(argv[1])
    else:
        port = 8080
    app.run(debug=False, host="0.0.0.0", port=port)
