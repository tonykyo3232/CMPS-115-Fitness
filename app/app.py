from flask import Flask, render_template, request, jsonify
from utils import filter_programs, filter_routines, load_programs, load_routines, search_program
import pickle

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_home.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        print(request.form)

        '''
        test_opt = {
            "style": "Bodybuilding", #"General Fitness",
            "level": -1,
            "len_min": -1, #4,
            "len_max": -1,#8,
            "goal": "" #"Build Muscle"
        }
        '''
        
        form = request.form
        length_opt = form.get("length", "-1,-1")
        len_min = int(length_opt.split(",")[0])
        len_max = int(length_opt.split(",")[1])
        opt = {
            "style": form.get("style", ""),
            "level": int(form.get("level", "-1")),
            "len_min": len_min,
            "len_max": len_max,
            "goal": form.get("goal", "")
        }
        
        target = form.get("target", "").lower()
        if target == "program":
            programs = load_programs()
            return render_template("search.jinja", programs=filter_programs(programs, opt))
        elif target == "routine":
            routines = load_routines()
            return render_template("search.jinja", programs=filter_routines(routines, opt))
        else:
            programs = load_programs()
            return render_template("search.jinja", programs=programs)
    else:
        programs = load_programs()
        return render_template("search.jinja", programs=programs)


@app.route("/detail", methods=["GET"])
def detail():
    programs = load_programs()

    # program = search_program(programs, program_id)
    program = programs[1]
    return render_template("detail.jinja", program=program)


@app.route("/customize", methods=["GET", "POST"])
def customize():
    if request.method == "POST":
        workout = request.get_json()
        return "Not implemented"
    else:
        return render_template("customize.html")


@app.route("/program/detail/<int:program_id>", methods=["GET"])
def program_detail(program_id):
    programs = load_programs()

    program = search_program(programs, program_id)
    if program == None:
        return "Such program doesn't exist."
    return render_template("detail.jinja", program=program)


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
