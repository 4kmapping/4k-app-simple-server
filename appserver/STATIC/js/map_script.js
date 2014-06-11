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

  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions); 
    
  setMarkers(32.807693, 34.997254);
}

function setMarkers(lat, lng) {

	var coord = new google.maps.LatLng(lat,lng);
	
    var marker = new google.maps.Marker({
      position: coord,
      map: map,
      animation: google.maps.Animation.DROP
     });
    markersArray.push(marker);

    google.maps.event.addListener(marker, 'click', function(event){
      popInfoWindow(marker, coord);
    });
     
}

function popInfoWindow(marker, coord)
{
		var geocoder = new google.maps.Geocoder();
	    // map.setCenter(latlng);
		
		var contentString = 
			'<div id = "content">' +
			'<h1 id = "Heading" class = "Heading" >  </h1>' +
			'<div id = "bodyContent">';
		
		geocoder.geocode({'latLng': coord}, function(results, status) 
		{
			if (status == google.maps.GeocoderStatus.OK) 
			{
				if (results[1]) 
				{
					contentString += '<p> Address :' + results[1].formatted_address+ '</p>';
				}
			}
			
			contentString +=
			  '<p> latitude, longitude : ' +'<b>' + coord.lat() +' '+ coord.lng() +'</b></p>' +
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
	);
}




function home()
{
	map.setZoom(myzoom);
	map.setCenter(LntLagCenter);
}




function getLocations()
{
	var json = $("#locations").text();
	//alert(json);
	
	json = $.parseJSON(json);
	
	
	for( i = 0 ; i < json.length ; i ++ )
	{
		var loc = json[i];
		setMarkers(loc.fields.latitude, loc.fields.longitude);
	}
	
}



//google.maps.event.addDomListener(window, 'load', initialize);


$(document).ready(function()
{
	initialize();
	getLocations();
	
	getMapData();
});