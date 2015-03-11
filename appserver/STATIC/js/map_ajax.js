function getMapData()
{
	$.ajax({
		type: "GET"
		, url: "http://localhost:8000/api/0.1/location"
		, dataType: "JSON"
		, beforSend: function(xhr)
		{
			xhr.setRequestHeader("Content-Type","application/json");
			xhr.setRequestHeader("Accept","application/json");
			xhr.setRequestHeader("Authorization", "ApiKey tester:1a2b3c4d5e");
		}
		, success: function(data)
		{
			alert(data);
		}
	});
}