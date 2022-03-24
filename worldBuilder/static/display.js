let plant1 = document.getElementById("plant1") //Row 1 Plants
let plant2 = document.getElementById("plant2")
let plant3 = document.getElementById("plant3")
let plant4 = document.getElementById("plant4") // Row 2 Plants
let plant5 = document.getElementById("plant5")
let plant6 = document.getElementById("plant6")
let plant7 = document.getElementById("plant7") // Row 3 Plants
let plant8 = document.getElementById("plant8")
let plant9 = document.getElementById("plant9")

text1 = document.getElementById('text1').textContent
text2 = document.getElementById('text2').textContent
text3 = document.getElementById('text3').textContent
text4 = document.getElementById('text4').textContent
text5 = document.getElementById('text5').textContent
text6 = document.getElementById('text6').textContent
text7 = document.getElementById('text7').textContent
text8 = document.getElementById('text8').textContent
text9 = document.getElementById('text9').textContent

textReplace1 = document.getElementById('text1')
textReplace2 = document.getElementById('text2')
textReplace3 = document.getElementById('text3')
textReplace4 = document.getElementById('text4')
textReplace5 = document.getElementById('text5')
textReplace6 = document.getElementById('text6')
textReplace7 = document.getElementById('text7')
textReplace8 = document.getElementById('text8')
textReplace9 = document.getElementById('text9')

reward1 = document.getElementById('reward1')
reward2 = document.getElementById('reward2')
reward3 = document.getElementById('reward3')
reward4 = document.getElementById('reward4')
reward5 = document.getElementById('reward5')
reward6 = document.getElementById('reward6')

var textReplace = [textReplace1,textReplace2,textReplace3,textReplace4,textReplace5,textReplace6,textReplace7,textReplace8,textReplace9]
var textOutputs = [text1,text2,text3,text4,text5,text6,text7,text8,text9]
var plantDisplay = [plant1,plant2,plant3,plant4,plant5,plant6,plant7,plant8,plant9]
var rewards = [reward1,reward2,reward3,reward4,reward5,reward6]

building = []
streakNumber = []


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
        console.log(data)
    });


setTimeout(function getPlants() {

    console.log(getObj())

    for (var i=0; i<textOutputs.length; i++) {
        building.push(textOutputs[i].substring(0,textOutputs[i].length-1))
        streakNumber.push(textOutputs[i].slice(-1))
    }
    console.log(building)

    console.log(streakNumber)
    console.log(document.getElementById('text7').textContent)


    plantTypes = []

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
        if (parseInt(streakNumber[i])>3){
            parseInt(streakNumber[i])
            level = "3";
        }
        else if (parseInt(streakNumber[i])>1){
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

        if (streakNumber[i].localeCompare("0") === 0) {
            var directory =  preDirectory.concat("empty.png")
            plantDisplay[i].src = directory;
            plantDisplay[i].style.display = "inline-block";
            textReplace[i].innerHTML = "";
        } else{
            var directory = preDirectory.concat(plantImages[i])
            plantDisplay[i].src = directory;
            plantDisplay[i].style.display = "inline-block";

        }
    }

    //DISPLAYING REWARDS

    for (var i=0; i<rewards.length; i++) {
        console.log(rewards[i].src.slice(-3))
        if (rewards[i].src.slice(-3).localeCompare("png") != 0){
            console.log("remove")
            rewards[i].style.display = "none"
        }
    }

}, 200);