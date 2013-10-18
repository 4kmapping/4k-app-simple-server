$(document).ready(function(){

    var map = L.map('map').setView([52.3731, 4.8922], 4);

    L.tileLayer('http://{s}.tile.cloudmade.com/8E10386EF81C4270B374C76464C939C2/997/256/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
        maxZoom: 18
    }).addTo(map);

    $.ajax({
        url: '/api/0.1/location/',
        // crossDomain: true,
        // contentType: 'application/json',
        beforeSend: function(request){
            request.setRequestHeader('Authorization', 'ApiKey joshua:yolo');
        },
        success: function(data){

            $.each(data.objects, function(index, location){

                L.marker([location.lat, location.lon]).addTo(map);

            }) ;

        }
    }) ;



}) ;