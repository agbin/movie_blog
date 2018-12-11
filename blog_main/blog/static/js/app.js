$(document).ready(function() {

    if (window.jQuery) {
        // jQuery is loaded
        alert("Yeah!");
        console.log( "ready!" );
    } else {
        // jQuery is not loaded
        alert("Doesn't Work");
    }

});