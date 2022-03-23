let output = document.getElementById("displayOutput")

let plant1 = document.getElementById("plant1") //Row 1 Plants
let plant2 = document.getElementById("plant2")
let plant3 = document.getElementById("plant3")
let plant4 = document.getElementById("plant4") // Row 2 Plants
let plant5 = document.getElementById("plant5")
let plant6 = document.getElementById("plant6")
let plant7 = document.getElementById("plant7") // Row 3 Plants
let plant8 = document.getElementById("plant8")
let plant9 = document.getElementById("plant9")

let text1 = document.getElementById("text1") // Row 1 Text
let text2 = document.getElementById("text2")
let text3 = document.getElementById("text3")
let text4 = document.getElementById("text4") // Row 2 Text
let text5 = document.getElementById("text5")
let text6 = document.getElementById("text6")
let text7 = document.getElementById("text7") // Row 3 Text
let text8 = document.getElementById("text8")
let text9 = document.getElementById("text9")

var plantDisplay = [plant1,plant2,plant3,plant4,plant5,plant6,plant7,plant8,plant9]
var textDisplay = [text1,text2,text3,text4,text5,text6,text7,text8,text9]


"use strict";

let mainObj = {};
/**
 * Allows JSON data to be acquired by other functions
 * @returns {Object} holds the config.JSON data
 */
let getObj = function() {
    for (let prop in mainObj) {
        return mainObj[prop];
    }
}

fetch("../../static/config.json") //Loads JSON data into JavaScript program
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        mainObj = data;
    });


let name = document.getElementById('username');
name = name.textContent.trim();
name = name.substring(0, name.length-10);
console.log(name)
userProfileDirectory =  "../../static/Users/".concat(name);
userProfileDirectory = userProfileDirectory.concat(".txt");
console.log(userProfileDirectory);

var profileInfo
fetch(userProfileDirectory)
.then(response => response.text())
.then(data => {
    profileInfo = data
    console.log(profileInfo)
});


//Example input for full Profile Page
var building = ["Harrison Building", "Amory Building", "Great Hall", "The Forum", "Northcott Theatre",
"Innovation One SWIoT", "Library", "Peter Chalk Centre", "Geoffrey Pope"];
var streaks = ["1","4","5","7","3","2","7","3","5"];
var lastAccessed = [];
var plantTypes  = [];  // Data retrieved from config.json

setTimeout(function getPlants(){

    //Loading .txt data
    console.log(profileInfo)

    var profileLines = profileInfo.split("\r" + "\n")

    console.log(profileLines)


    var globalLogin = profileLines[0].split(",")
    console.log(globalLogin) //GLOBAL LOGIN DETAILS

    var building = [];
    var streaks = [];
    var lastAccessed = [];


    for (i = 1; i<profileLines.length-1; i++) {
        var tempArray = profileLines[i].split(',')
        console.log(tempArray)


        if (tempArray[1].localeCompare("0") != 0) {
            building.push(tempArray[0])
            streaks.push(tempArray[1])
            lastAccessed.push(tempArray[2])
            console.log(tempArray)

        }

    }

    console.log(building)
    console.log(streaks)

    console.log(lastAccessed)


    //Loading .JSON data for plant type
    for (var i = 0; i<building.length; i++) {
        for (var j = 0; j<getObj().length; j++) {
            if (building[i].localeCompare(getObj()[j].name) === 0) {
                plantTypes.push(getObj()[j].type)
                break;
            }
        }
    }

    // Calculating the "plant level"
    var plantImages = [];
    for (var i=0; i < building.length; i++) {
        var level = "1";
        if (parseInt(streaks[i])>3){
            parseInt(streaks[i])
            level = "3";
        }
        else if (parseInt(streaks[i])>1){
            level = "2";
        }

        //Creating file names to be concatenated with the preDirectory, file names stored into plantName array
        var plantName = plantTypes[i].concat(level);
        plantName = plantName.concat(".png");
        plantImages.push(plantName);
        console.log(plantName);
        console.log(plantImages[i])
    }

    //Displaying plant images into plant.innerHTML elements
    let preDirectory = "../../static/plants/"
    for (var i=0; i <building.length; i++) {

        var directory = preDirectory.concat(plantImages[i])
        plantDisplay[i].src = directory;
        plantDisplay[i].style.display = "inline-block";
    }

    //Displaying streak text into text.innerHTML elements

    for (var i=0; i < building.length; i++) {
        textDisplay[i].innerHTML = building[i];
        textDisplay[i].style.display = "inline-block";
    }

}, 150);