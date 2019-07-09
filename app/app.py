from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, world!"

@app.route("/api/programs")
def program_api():
    if request.method == "GET":
        with open("program_dict.pickle", "rb") as fp:
            prog_dict = pickle.load(fp)
        
        # prog_dict should be replaced with acceptable dictionary example for workout programs...
        return jsonify([prog_dict])
    else:
        return "Not implemented"

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        port = int(argv[1])
    else:
        port = 8080
    app.run(debug=False, host="0.0.0.0", port=port)
