function collect_exercise_meta(exercise_elem) {
    // collect all exercise meta data from the given exercise element (which will highly be div element)
    var exercise = {
      name: exercise_elem.querySelector(".exercise-name"), // TODO: acquire value from the element
      // type
      // order
      length: exercise_elem.querySelector(".exercise-length"),
      weight: exercise_elem.querySelector(".exercise-weight"),
      rpe: exercise_elem.querySelector(".exercise-rpe"),
      note: exercise_elem.querySelector(".exercise-note")
    }

    return exercise;
}
  
function collect_day_meta(day_elem) {
    // collect all day meta data from the given day element (which will highly be div element)
    
    // collect meta data
    var day = {
      name: day_elem.querySelector(".day-name") // TODO: acquire value from the element
    }

    // iterate each exercise and store it in day_elem.exercises
    var exercises = [];
    var exercise_elems = document.querySelectorAll(".exercise");
    for (let exercise_idx = 0; exercise_idx < exercise_elems.length; exercise_idx++) {
      let exercise = collect_exercise_meta(exercise_elems[exercise_idx]);
      exercises.push(exercise);
    }
    day["exercises"] = exercises;
    return day;
}
  
function collect_cycle_meta(cycle_elem) {
    // collect all cycle meta data from the given cycle element (which will highly be div element)
    
    // collect meta data
    var cycle = {
      name: cycle_elem.querySelector(".cycle-name") // TODO: acquire value from the element
    };

    // iterate each day and store it in cycle_elem.days
    var days = [];
    var day_elems = document.querySelectorAll(".day");
    for (let day_idx = 0; day_idx < day_elems.length; day_idx++) {
      let day = collect_day_meta(day_elems[day_idx]);
      days.push(day);
    }
    cycle["days"] = days;
    return cycle;
}
  
  function collect_workout() {
    var workout = {
      type: document.querySelector(".workout-type"), // TODO: acquire value from the element
      styles: document.querySelector(".workout-style"),
      level: document.querySelector(".workout-level"),
      length: document.querySelector(".workout-length"),
      goals: document.querySelector(".workout-goal"),
      desc: document.querySelector(".workout-desc")
    };

    var cycles = [];
    var cycle_elems = document.querySelectorAll(".cycle");
    for (let cycle_idx = 0; cycle_idx < cycle_elems.length; cycle_idx++) {
      let cycle = collect_cycle_meta(cycle_elems[cycle_idx]);
      cycles.push(cycle);
    }
    workout["cycles"] = cycles;

    return workout;
  }

  // function nested_clear(elem) {
  //   elem.querySelectorAll("input")
  // }