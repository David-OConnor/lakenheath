"use strict";

var map;

function initialize() {
    var mapOptions = {
        zoom: zoom,
        center: new google.maps.LatLng(centerRaw[0], centerRaw[1]),

        // Ideally pass this from views.py, but can't cleanly set this constructor
        // without a series of if statements.
        mapTypeId: google.maps.MapTypeId.SATELLITE
    };

    // Declare map globally so it can be used elsewhere.
    map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);

    // Import maplabels.
    var script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = '/static/js/maplabel.js';
        document.body.appendChild(script);
}

function loadScript() {
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp' +
        '&signed_in=true&callback=initialize';
    document.body.appendChild(script);
}

window.onload = loadScript;




