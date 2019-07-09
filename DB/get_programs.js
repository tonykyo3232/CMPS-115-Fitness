/*
const host = "http://ec2-18-217-233-23.us-east-2.compute.amazonaws.com:8080";

// Asynchronous version using fetch API
fetch(host + '/api/programs')
.then(function(response){
    return response.json();
})
.then(function(programs){
    console.log(programs);
})
*/

// Synchronous version using XMLHttpRequest
const host = "http://ec2-18-217-233-23.us-east-2.compute.amazonaws.com:8080";

var xhr = new XMLHttpRequest();
xhr.open("GET", host + "/api/programs", false);
xhr.send();
var programs = JSON.parse(xhr.responseText);

console.log(programs);
