const x = document.getElementById("map");
const y = document.getElementById("pointer");
const output = document.getElementById("output");



//This Data will be moved into config.json
const latitudeTop = 50.740142;
const longitudeLeft = -3.538104;
const latitudeBot = 50.731926;
const longitudeRight = -3.524936;
const xDifference = Math.abs(longitudeLeft-longitudeRight)
const yDifference = Math.abs(latitudeTop-latitudeBot)


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

fetch("../static/config.json") //Loads JSON data into JavaScript program
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        mainObj = data;

    });


/**
 * Checks if the browser supports Geolocation API
 * If so, showPosition is executed
 */

setTimeout(

function getLocation() {
    console.log(getObj())
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);


    } else {
        output.innerHTML = "Geolocation is not supported by this browser.";

    }
}, 200);

/**
 * Holds the main logic for pointing to the player's locations on the map
 * and identifying if the player is standing near any buildings
 * @param position is the
 */

function showPosition(position) {


    let currentLatitude = position.coords.latitude;
    let currentLongitude = position.coords.longitude;

    //Harrison Building coordinates, Use this space to test different locations remotely
    //


    if ((currentLatitude<latitudeTop && currentLatitude>latitudeBot) //Checks if player coords are within campus
        && (currentLongitude>longitudeLeft && currentLongitude<longitudeRight)) {

        //calculating relativeCoordinates of players current location
        let i;
        const yPosition = (Math.abs(latitudeTop - currentLatitude))/yDifference;
        const xPosition = (Math.abs(longitudeLeft - currentLongitude))/xDifference;
        let htmlYPosition = Math.round(yPosition*100);
        let htmlXPosition = Math.round(xPosition*100);

        //Altering .css properties of pin.png to point towards the players location
        const pin = document.getElementById("pointer");
        pin.style.top = htmlYPosition-5 + "%";
        pin.style.left = htmlXPosition-2 + "%";
        pin.style.width = "5%";

        // Initializing variables to store the name, latitudes and longitudes of locations in config.json
        // Loading data every time can be computationally expensive, there may be a more efficient approach
        const locations = [];
        let latitudes = [];
        let longitudes = [];
        const relativeLatitudes = []; //relativeCoordinates (See Specification)
        const relativeLongitudes = []; //relativeCoordinates (See Specification)

        for (i = 0; i<getObj().length; i++) { //Storing .json data into initialized lists
            console.log(getObj()[i].name);
            locations.push(getObj()[i].name);
            latitudes.push(parseFloat(getObj()[i].latitude));
            longitudes.push(parseFloat(getObj()[i].longitude));
        }
        for (i = 0; i<latitudes.length; i++) { //Calculating relative coordinates and storing into initialized lists
            relativeLatitudes.push(Math.abs((latitudeTop-latitudes[i]))/yDifference);
            relativeLongitudes.push(Math.abs((longitudeLeft-longitudes[i]))/xDifference);
        }

        console.log(relativeLongitudes)
        console.log(relativeLatitudes)

        let outputText = "";
        var getOutput = [];
        for (i = 0; i<relativeLongitudes.length; i++) {
            let y = relativeLatitudes[i]-yPosition;
            let x = relativeLongitudes[i]-xPosition;
            console.log(Math.sqrt(x*x + y*y))
            if (Math.sqrt(x*x + y*y)<0.1) {

                if (outputText.localeCompare("") === 0) {
                    outputText += " "+locations[i];
                    getOutput.push(locations[i])
                } else {
                    outputText += " & "+locations[i];
                    getOutput.push(locations[i])

                }
            }
        }

        if (outputText.localeCompare("") === 0) {
            output.innerHTML = "You don't seem to be near any buildings, keep looking!"
        }else {
            output.innerHTML = "You are near " + outputText





        }

    } else { //Current coordinates are outside the bounds of the campus coordinates
        console.log (currentLatitude + ", " + currentLongitude)

        console.log ("The player is outside the university")
        output.innerHTML = "You are outside the university";


    }


}


function triggerPython() {
    let buildingName = document.getElementById('output').textContent;
    buildingName = buildingName.substring(14)




    var outputThis = "../simple_function?" + buildingName

    window.location.href = outputThis
    // simple_function?buildingname & buildingname?
    //window.location.href = "../simple_function?whatever";

};