from flask import Flask, render_template, request, jsonify
#from flask_pymongo import PyMongo
from utils import filter_programs, filter_routines, SimpleDataManager
import pickle

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/fitness"
#mongo = PyMongo(app)
sdm = SimpleDataManager()


@app.route("/")
def index():
    return render_template("index_home.jinja")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass
    else:
        return render_template("index_login.jinja")

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
            return render_template("search.jinja", programs=filter_programs(sdm.programs, opt))
        elif target == "routine":
            return render_template("search.jinja", programs=filter_routines(sdm.routines, opt))
        else:
            return render_template("search.jinja", programs=sdm.programs)
    else:
        return render_template("search.jinja", programs=sdm.programs)


@app.route("/customize", methods=["GET", "POST"])
def customize():
    if request.method == "POST":
        workout_input = request.get_json()
        
        # check input
        #try:
        is_routine = False if workout_input["type"] == "Program" else True
        item = {
            "name": workout_input["name"],
            "styles": workout_input["styles"],
            "level": workout_input["level"],
            "length": workout_input["length"],
            "goals": workout_input["goals"],
            "desc": workout_input["desc"],
            "cycles": workout_input["cycles"],
            "is_routine": is_routine
        }
        # TODO: validate cycles - days - exercises recursively
        # TODO: validate whether routine contains only 1 cycle - 1 day
        
        if is_routine:
            sdm.insert_custom_routine(item)
        else:
            sdm.insert_custom_program(item)
        return jsonify({"code": 200, "message": "Successfully inserted"})
        #except:
        #    return jsonify({"code": 500, "message": "Wrong workout input"})
    else:
        return render_template("customize.jinja")

@app.route("/overview", methods=["GET", "POST"])
def overview():
	if request.method == "POST":
		workout_input = request.get_json()
		
		is_routine = False if workout_input["type"] == "Program" else True
		item = {
			"name": workout_input["name"],
			"styles": workout_input["styles"],
			"level": workout_input["level"],
			"length": workout_input["length"],
			"goals": workout_input["goals"],
			"desc": workout_input["goals"],
			"cycles": workout_input["cycles"],
			"is_routine": is_routine
		}
		return render_template("overview.jinja", program=workout_input)
	else:
		workout_input = request.get_json()
		item = {
			"name": workout_input["name"],
			"styles": workout_input["styles"],
			"level": workout_input["level"],
			"length": workout_input["length"],
			"goals": workout_input["goals"],
			"desc": workout_input["goals"],
			"cycles": workout_input["cycles"],
			"is_routine": is_routine
		}
		return render_template("overview.jinja", program=workout_input)

@app.route("/program/detail/<int:program_id>", methods=["GET"])
def program_detail(program_id):
    program = sdm.search_item(is_routine=False, _id=program_id)
    if program == None:
        return "Such program doesn't exist."
    return render_template("detail.jinja", program=program)

@app.route("/api/programs")
def get_all_programs():
    if request.method == "GET":
        return jsonify(sdm.programs)
    else:
        return "Not implemented"

@app.route("/routine/detail/<int:routine_id>", methods=["GET"])
def routine_detail(routine_id):
    routine = sdm.search_item(is_routine=True, _id=routine_id)
    if routine == None:
        return "Such routine doesn't exist."
    return render_template("detail.jinja", program=routine)

@app.route("/api/routines")
def get_all_routines():
    if request.method == "GET":
        return jsonify(sdm.routines)
    else:
        return "Not implemented"

@app.route("/index_how_to")
def how_to():
    return render_template("index_how_to.html")

@app.route("/index_htResult")
def how_to_result():
    return render_template("index_htResult.html")

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        port = int(argv[1])
    else:
        port = 8080
    app.run(debug=False, host="0.0.0.0", port=port)
