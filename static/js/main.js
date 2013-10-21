    //for jshint to stop crying
var $ = $,
    L = L,
    d3 = d3,
    //them app!
    app = {

        data: [],

        init: function(){

            //bind stuff
            $(document).on('submit', '#api_info', app.handleLogin) ;
            $(document).on('click', 'header .toggle a:not(.selected)', app.handleToggle) ;

            //get the party started

            //if the user doesn't have api info saved already
            if(localStorage.api_name === undefined && localStorage.api_key === undefined){

                //show log in form
                app.showLogin() ;

            }
            else {

                //fetch some data
                $.ajax({
                    url: '/api/0.1/location/',
                    beforeSend: function(request){
                        request.setRequestHeader('Authorization', 'ApiKey ' + localStorage.api_name + ':' + localStorage.api_key);
                    },
                    success: function(data){

                        app.data = data.objects ;
        
                        //show header!
                        $('header').fadeIn() ;

                        //start with the map
                        app.loadMap();

                    },
                    error: function(){
                
                        $('.main p').html('Your api info is wrong, please try again.') ;

                    }
                }) ;

            }

        },

        //logging in functionality!
        showLogin: function(){
            $('#api_info').fadeIn() ;
        },
        handleLogin: function(){

            var $this = $(this) ;

            localStorage.api_name = $this.find('input[name="api_name"]').val() ;
            localStorage.api_key = $this.find('input[name="api_key"]').val();

            $this.fadeOut();

            app.init() ;

            return false ;

        },

        handleToggle: function(){

            var $toggle = $('header .toggle'),
                toHide = $toggle.find('.selected').data('screen'),
                toShow = $(this).data('screen') ;

            $('#' + toHide).remove() ;
            app['load' + toShow.capitalize()]() ; //black magic

            $('header .toggle a').removeClass('selected') ;
            $(this).addClass('selected') ;

        },

        loadMap: function(){

            if($('#map').length > 0) $('#map').remove();
            $('section').prepend('<div id="map"></div>') ;

            var map = L.map('map').setView([52.3731, 4.8922], 4);

            L.tileLayer('http://{s}.tile.cloudmade.com/8E10386EF81C4270B374C76464C939C2/997/256/{z}/{x}/{y}.png', {
                attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
                maxZoom: 18
            }).addTo(map);

            $.each(app.data, function(index, location){

                L.marker([location.lat, location.lon]).addTo(map);

            }) ;

        },
        loadStats: function(){

            var totalTags = 0,
                totalTagOccurrences = {} ;

            //some data processing goin' on
            $.each(app.data, function(){
                
                //making sure tags is an array
                if(typeof this.tags === 'string') {
                    this.tags = $.parseJSON(this.tags.replace(/u'/g, "'").replace(/'/g, '"')) ;
                }

                //adding toward the total tags
                totalTags = totalTags + this.tags.length ;

                $.each(this.tags, function(index, value){

                    if(totalTagOccurrences[value] === undefined) {
                        totalTagOccurrences[value] = 0 ;
                    }

                    totalTagOccurrences[value] = totalTagOccurrences[value] + 1 ;

                }) ;

            }) ;

            var totalTagOccurrencesTags = Object.keys(totalTagOccurrences),
                totalTagOccurrencesValues = [] ;

            $.each(totalTagOccurrences, function(index, value){
                totalTagOccurrencesValues.push(value) ;
            }) ;

            if($('#stats').length > 0) $('#stats').remove();
            $('section').prepend('<div id="stats"></div>') ;

            $('#stats').append('<p class="stat"><span class="number">' + app.data.length + '</span><br> total locations</p>') ;
            $('#stats').append('<p class="stat"><span class="number">' + totalTags + '</span><br> total tag entries</p>') ;
            $('#stats').append('<p class="stat"><span class="number">' + totalTagOccurrencesTags.length + '</span><br> unique tags</p>') ;

            var topTags = d3.select('#stats')
                            .append('svg')
                            .attr('class', 'chart')
                            .attr('width', 420)
                            .attr('height', 40 * totalTagOccurrencesValues.length) ;

            var x = d3.scale.linear()
                    .domain([0, d3.max(totalTagOccurrencesValues)])
                    .range([0, 440]);

            topTags.selectAll("rect")
                    .data(totalTagOccurrencesValues)
                    .enter().append("rect")
                    .attr("y", function(d, i) { return i * 40; })
                    .attr("width", x)
                    .attr("height", 40);

            topTags.selectAll("text")
                    .data(totalTagOccurrencesValues)
                    .enter().append("text")
                    .attr("x", x)
                    .attr("y", function(d, i) { return i * 40 + 20; })
                    .attr("dx", -10) // padding-right
                    .attr("dy", ".35em") // vertical-align: middle
                    .attr("text-anchor", "end") // text-align: right
                    .text(String);

            topTags.selectAll("label")
                    .data(totalTagOccurrencesTags)
                    .enter().append("text")
                    .attr("x", x)
                    .attr("y", function(d, i) { return i * 40 + 20; })
                    .attr("dx", 10) // padding-right
                    .attr("dy", ".35em") // vertical-align: middle
                    .attr("text-anchor", "left") // text-align: right
                    .text(String);

        }
    } ;

$(document).ready(function(){
    app.init() ;
}) ;