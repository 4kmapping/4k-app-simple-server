//for jshint to stop crying
var $ = $,
    L = L ;

$(document).ready(function(){

    var showLogin = function(){
        $('#api_info').fadeIn() ;
    } ;

    $('#api_info').submit(function(){

        var $this = $(this),
            name = $this.find('input[name="api_name"]').val(),
            key = $this.find('input[name="api_key"]').val() ;

        localStorage.api_name = name ;
        localStorage.api_key = key ;

        $this.fadeOut();

        init() ;

        return false ;

    }) ;

    var loadMap = function(){

        if($('#map').length > 0) $('#map').remove();
        $('section').prepend('<div id="map"></div>') ;

        $.ajax({
            url: '/api/0.1/location/',
            beforeSend: function(request){
                request.setRequestHeader('Authorization', 'ApiKey ' + localStorage.api_name + ':' + localStorage.api_key);
            },
            success: function(data){

                var map = L.map('map').setView([52.3731, 4.8922], 4);

                L.tileLayer('http://{s}.tile.cloudmade.com/8E10386EF81C4270B374C76464C939C2/997/256/{z}/{x}/{y}.png', {
                    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
                    maxZoom: 18
                }).addTo(map);

                $.each(data.objects, function(index, location){

                    L.marker([location.lat, location.lon]).addTo(map);

                }) ;

            },
            error: function(){
        
        
                $('.main p').html('Your api info is wrong, please try again.') ;

            }
        }) ;

    } ;

    var init = function(){

        if(localStorage.api_name === undefined && localStorage.api_key === undefined){
            showLogin() ;
        }
        else {
            $('header').fadeIn() ;
            loadMap();
        }

    } ;

    init() ;

}) ;