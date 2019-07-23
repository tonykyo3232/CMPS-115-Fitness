from flask import Flask, render_template, request, jsonify, url_for, redirect, session
from flask_pymongo import PyMongo
from bson import ObjectId
from utils import filter_programs, filter_routines
import json
import bcrypt


class JSONEncoder(json.JSONEncoder):                           
    ''' extend json-encoder class'''
    def default(self, o):                               
        if isinstance(o, ObjectId):
            return str(o)                               
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/fitness"
mongo = PyMongo(app)
app.json_encoder = JSONEncoder


@app.route("/")
def index():
    return render_template("index_home.jinja")

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
            programs = mongo.db.workouts.find({"is_routine": False})
            return render_template("search.jinja", programs=filter_programs(programs, opt))
        elif target == "routine":
            routines = mongo.db.workouts.find({"is_routine": True})
            return render_template("search.jinja", programs=filter_routines(routines, opt))
        else:
            programs = mongo.db.workouts.find({"is_routine": False})
            return render_template("search.jinja", programs=programs)
    else:
        programs = mongo.db.workouts.find({"is_routine": False})
        return render_template("search.jinja", programs=list(programs))


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

        mongo.db.workouts.insert_one(item)
        return jsonify({"code": 200, "message": "Successfully inserted"})
        #except:
        #    return jsonify({"code": 500, "message": "Wrong workout input"})
    else:
        return render_template("customize.jinja")

		
@app.route("/overview/<workout>", methods=["GET"])
def overview(workout):
	return render_template("overview.jinja", program=workout)
		
		
@app.route("/overview", methods=["POST"])
def get_overview():
	workout_input = request.get_json()
	
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
	return render_template("overview.jinja", program=item)
		
@app.route("/detail/<program_id>", methods=["GET"])
def program_detail(program_id):
    program = mongo.db.workouts.find_one({"_id": ObjectId(program_id)})
    if program == None:
        return "Such program doesn't exist."
    return render_template("detail.jinja", program=program)

@app.route("/api/programs")
def get_all_programs():
    if request.method == "GET":
        programs = mongo.db.workouts.find({"is_routine": False})
        return jsonify(programs)
    else:
        return "Not implemented"

@app.route("/api/routines")
def get_all_routines():
    if request.method == "GET":
        routines = mongo.db.workouts.find({"is_routine": True})
        return jsonify(routines)
    else:
        return "Not implemented"

@app.route("/index_how_to")
def how_to():
    return render_template("index_how_to.jinja")

@app.route("/index_htResult")
def how_to_result():
    return render_template("index_htResult.html")


# ----- Account routers -----

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username' : request.form['username']})
        print(login_user)
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['user'] = {
                    'username': login_user['username'],
                    'nickname': login_user['nickname']
                }
                return redirect(url_for('index'))
        return 'Invalid username/password combination'
    else:
        return render_template("login.jinja")

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        username = request.form['username']
        nickname = request.form['nickname']
        existing_user = users.find_one({'username' : username})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({
                'username' : username,
                'password' : hashpass,
                'nickname' : nickname
            })
            session['user'] = {
                'username': username,
                'nickname': nickname
            }
            return redirect(url_for('index'))
        
        return 'That username already exists! Please try other username'

    return render_template('register.jinja')


if __name__ == "__main__":
    import random, string
    from sys import argv
    if len(argv) > 1:
        port = int(argv[1])
    else:
        port = 8080
    app.secret_key = ''.join(random.choice(string.ascii_lowercase) for i in range(32))
    app.run(debug=False, host="0.0.0.0", port=port)
