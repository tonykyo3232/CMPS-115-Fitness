// collect all exercise meta data from the given exercise element (which will highly be div element)
function collect_exercise_meta(exercise_elem) {
  
  // collect meta data
  var exercise = {
    name: exercise_elem.querySelector(".exercise-name").value,
    type: exercise_elem.querySelector(".exercise-type").value,
    equipment: exercise_elem.querySelector(".exercise-equipment").value.split(',').map(equip => equip.trim()),
    length: exercise_elem.querySelector(".exercise-length").value,
    weight: exercise_elem.querySelector(".exercise-weight").value,
    rpe: exercise_elem.querySelector(".exercise-rpe").value,
    notes: [exercise_elem.querySelector(".exercise-note").value]
  }

  return exercise;
}

// collect all day meta data from the given day element (which will highly be div element)
function collect_day_meta(day_elem) {
  
  // collect meta data
  var day = {
    desc: day_elem.querySelector(".day-desc").value
  }

  // iterate each exercise and store it in day_elem.exercises
  var exercises = [];
  var exercise_elems = day_elem.querySelectorAll(".exercise-container");
  for (let exercise_idx = 0; exercise_idx < exercise_elems.length; exercise_idx++) {
    let exercise = collect_exercise_meta(exercise_elems[exercise_idx]);
    exercises.push(exercise);
  }
  day["exercises"] = exercises;
  return day;
}

// collect all cycle meta data from the given cycle element (which will highly be div element)
function collect_cycle_meta(cycle_elem) {
  
  // collect meta data
  var cycle = {
    name: cycle_elem.querySelector(".cycle-name").value,
    length: parseInt(cycle_elem.querySelector(".cycle-length").value)
  };
  console.log(cycle);
  if (isNaN(cycle["length"])) {
    cycle["length"] = -1;
  }

  // iterate each day and store it in cycle_elem.days
  var days = [];
  var day_elems = document.querySelectorAll(".day-container");
  for (let day_idx = 0; day_idx < day_elems.length; day_idx++) {
    let day = collect_day_meta(day_elems[day_idx]);
    days.push(day);
  }
  cycle["days"] = days;
  return cycle;
}

function collect_workout() {

  // collect meta data
  var workout = {
    type: document.querySelector(".workout-type").value,
    name: document.querySelector(".workout-name").value,
    styles: document.querySelector(".workout-styles").value.split(',').map(style => style.trim()),
    level: parseInt(document.querySelector(".workout-level").value),
    length: document.querySelector(".workout-length").value,
    goals: document.querySelector(".workout-goals").value.split(',').map(goal => goal.trim()),
    desc: document.querySelector(".workout-desc").value
  };

  workout["length"] = workout["length"] === "" ? -1 : parseInt(workout["length"]);

  // iterate each cycle and store it in workout.cycles
  var cycles = [];
  var cycle_elems = document.querySelectorAll(".cycle-container");
  for (let cycle_idx = 0; cycle_idx < cycle_elems.length; cycle_idx++) {
    let cycle = collect_cycle_meta(cycle_elems[cycle_idx]);
    cycles.push(cycle);
  }
  workout["cycles"] = cycles;

  console.log(workout);
  return workout;
}

function get_cycle(workout){
	var cycle1 = workout.cycle[1];
	return cycle1;
}


function send_workout(workout) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/customize", false);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.send(JSON.stringify(workout));
  var result = JSON.parse(xhr.responseText);
  if (result["code"] === 200) {
    alert(result["message"]);
    document.location.reload();
  } else {
    alert(result["message"]);
  }
}

function show_workout(workout) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/overview", false);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.send(JSON.stringify(workout));
}