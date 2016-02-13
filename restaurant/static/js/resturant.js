 function validateForm()
 {
 	var showAlert = false;
 	var submit = true;
 	var password = document.forms["registrationform"]["password"].value;
 	var retypepassword = document.forms["registrationform"]["retype-password"].value;
 	var msg = "";

 	if (passwordmatch(password,retypepassword)==false)
 	{
 		msg = msg + "Passwords didn't match";
 		submit=false;
 		document.forms["registrationform"]["password"].parentNode.className="input-group has-error";
 		document.forms["registrationform"]["retype-password"].parentNode.className="input-group has-error";
 		alert(msg);
 	}
 		
 	return submit;
 }

function passwordmatch(password,retypepassword)
{
	if(password == retypepassword)
		return true;
	else
		return false;
}
	
function registrationmap()
		{
		    var latlng2 = new google.maps.LatLng(23.709921000000000000,90.407143000000020000);
		    var opts = {'center': latlng2, 'zoom':8, 'mapTypeId': google.maps.MapTypeId.ROADMAP }
		    var map = new google.maps.Map(document.getElementById('map-canvas'),opts);

		    var marker = new google.maps.Marker({position: latlng2, map: map});

	        google.maps.event.addListener(map,'click',function(event) {
		        document.getElementById('latitude-id').value = event.latLng.lat();
				document.getElementById('longitude-id').value = event.latLng.lng();
				var newlatlng = new google.maps.LatLng(event.latLng.lat(), event.latLng.lng());	
				marker.setPosition(newlatlng);	
		    })     
		}
google.maps.event.addDomListener(window, 'load', registrationmap);