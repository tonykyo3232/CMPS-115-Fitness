from flask import Flask, render_template, request, jsonify
from utils import filter_programs, filter_routines
import pickle

programs_file = "programs.pickle"
routines_file = "routines.pickle"

def load_programs():
    with open(programs_file, "rb") as fp:
        programs = pickle.load(fp)
    return programs

def load_routines():
    with open(routines_file, "rb") as fp:
        routines = pickle.load(fp)
    return routines

# search program by program_id
def search_program(programs, program_id):
    for program in programs:
        if program_id == program["program_id"]:
            return program
    return None

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        print(request.form)

        test_opt = {
            "style": "Bodybuilding", #"General Fitness",
            "level": -1,
            "len_min": -1, #4,
            "len_max": -1,#8,
            "goal": "" #"Build Muscle"
        }
        
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


@app.route("/program/detail/<program_id>", methods=["GET"])
def program_detail(program_id):
    programs = load_programs()

    program = search_program(programs, program_id)
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
