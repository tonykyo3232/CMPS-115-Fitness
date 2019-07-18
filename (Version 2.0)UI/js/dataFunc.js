// collect all exercise meta data from the given exercise element (which will highly be div element)
function collect_exercise_meta(exercise_elem) {
  
  var exercise = {
    name: exercise_elem.querySelector(".exercise-name").value, // TODO: acquire value from the element
    type: exercise_elem.querySelector(".exercise-type").value,
    order: exercise_elem.querySelector(".exercise-order").value,
    length: exercise_elem.querySelector(".exercise-length").value,
    weight: exercise_elem.querySelector(".exercise-weight").value,
    rpe: exercise_elem.querySelector(".exercise-rpe").value,
    note: exercise_elem.querySelector(".exercise-note").value
  }

  return exercise;
}

// collect all day meta data from the given day element (which will highly be div element)
function collect_day_meta(day_elem) {
  
  // collect meta data
  var day = {
    name: day_elem.querySelector(".day-name").value
  }

  // iterate each exercise and store it in day_elem.exercises
  var exercises = [];
  var exercise_elems = document.querySelectorAll(".exercise-container");
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
    name: cycle_elem.querySelector(".cycle-name").value
  };

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
  var workout = {
    type: document.querySelector(".workout-type").value, // TODO: acquire value from the element
    styles: document.querySelector(".workout-styles").value,
    level: document.querySelector(".workout-level").value,
    length: document.querySelector(".workout-length").value,
    goals: document.querySelector(".workout-goals").value,
    desc: document.querySelector(".workout-desc").value
  };

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

function send_workout(workout) {
  //const host = "http://ec2-18-217-233-23.us-east-2.compute.amazonaws.com:8080";
  const host = "localhost";

  var xhr = new XMLHttpRequest();
  xhr.open("POST", host + "/program/upload", false);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.send(JSON.stringify(workout));
}



// function nested_clear(elem) {
//   elem.querySelectorAll("input")
// }