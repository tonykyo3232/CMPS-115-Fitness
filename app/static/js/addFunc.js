//***************************************************
// function for extending the input field
// Using JavaScript function to create the code of HTML
//***************************************************

const exerciseHTML = document.querySelector(".exercise-container").innerHTML;

const dayHTML = document.querySelector(".day-container").innerHTML;

const cycleHTML = document.querySelector(".cycle-container").innerHTML;

function addExercise(button){

    var exerciseBody = document.createElement("div");
    exerciseBody.setAttribute("class","exercise-container");

    // assign the entire content inside the div tag
    exerciseBody.innerHTML = exerciseHTML;

    var addExerciseRow = button.parentNode.parentNode;
    var parent = addExerciseRow.parentNode;
    parent.insertBefore(exerciseBody, addExerciseRow);
}

function addDay(button){

    var dayBody = document.createElement("div");
    dayBody.setAttribute("class","day-container");

    // assign the entire content inside the div tag
    dayBody.innerHTML = dayHTML;

    var addDayRow = button.parentNode.parentNode;
    var parent = addDayRow.parentNode;
    parent.insertBefore(dayBody, addDayRow);
}

function addCycle(button){

    var cycleBody = document.createElement("div");
    cycleBody.setAttribute("class","cycle-container");

    // assign the entire content inside the div tag
    cycleBody.innerHTML = cycleHTML;

    var addCycleRow = button.parentNode.parentNode;
    var parent = addCycleRow.parentNode;
    parent.insertBefore(cycleBody, addCycleRow);
}