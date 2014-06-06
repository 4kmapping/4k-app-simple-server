var LntLagCenter = new google.maps.LatLng(33.65, 65.36); 

var lat;
var lng;

var iterator = 0;
var markersArray = [];
var map;
var infowindow = new google.maps.InfoWindow();
var myzoom;
function initialize() 
{
  lat = "32.807693";
  lng = "34.997254";
  var myLatLng = new google.maps.LatLng(lat,lng);
  var mapOptions;
  
  
  if($(window).width() > 1280)
  {
	myzoom = 4;
	
  }
  else
  {
	myzoom = 3;
  }
  

  var mapOptions = {
	zoom: myzoom,
	center: LntLagCenter,
	mapTypeId : google.maps.MapTypeId.ROADMAP
  };

  map = new google.maps.Map(document.getElementById('map-canvas'),
                                mapOptions); 
    
  setMarkers(myLatLng);
}

function setMarkers(latlng) { 
    marker = new google.maps.Marker({
      position: latlng,
      map: map,
      animation: google.maps.Animation.DROP
     });
    markersArray.push(marker);

      google.maps.event.addListener(marker, 'click', function(event){
         popInfoWindow(latlng);
      });
     
  }

function popInfoWindow(latlng)
{
		var geocoder = new google.maps.Geocoder();
	    // map.setCenter(latlng);
		geocoder.geocode({'latLng': latlng}, function(results, status) 
		{
			if (status == google.maps.GeocoderStatus.OK) 
			{
				if (results[1]) 
				{
					var contentString = 
					'<div id = "content">' +
					'<h1 id = "Heading" class = "Heading" >  </h1>' +
					'<div id = "bodyContent">'+
					  '<p> Address :' + results[1].formatted_address+ '</p>'+
					  '<p> latitude, longitude : ' +'<b>' + lat +' '+ lng +'</b></p>' +
					  '<p> bibleStudyType : <b> true </b> </p>' +
					  '<p> contactEmail :  <b> gch3339@gmail.com </b> </p>'+
					  '<p> contactPhone : <b> 010-2051-6869</b> </p>' +
					  '<p> indigenousType: <b> true </b> </p>'+
					  '<p> youthType : <b> true </b> </p>'+
					'</div>'+
					'</div>';

					map.setZoom(14);
					map.setCenter(marker.position);

					infowindow.setContent(contentString);
					infowindow.open(map, marker);
				} 
			}
		}	
	);
}




function home()
{
	map.setZoom(myzoom);
	map.setCenter(LntLagCenter);
}




function getLocations()
{
	$.ajax(
	{
		type:"GET",
		url:"http://192.237.166.7/api/0.1/location/",
		dataType:"jsonp",
		jsonp: "callback",
		beforeSend: function(jqXHR, settings) 
		{
		  jqXHR.setRequestHeader("Authorization","ApiKey junwon:1q2w3e4r5t");
	    },
		success: function(data)
		{
		
		
			alert("OK!!!!!");
		}
	});
}



google.maps.event.addDomListener(window, 'load', initialize);


$(document).ready(function()
{
	getLocations();
});