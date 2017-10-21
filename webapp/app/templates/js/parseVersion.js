$.ajax({
	type: "GET",
	url: "http://192.168.20.44:5000/getAvailableVersions",
	dataType: "json",
	success: function(data) {

		for (i= 0; i < len(data.versions); i++){
			console.log(data.versions[i])	
		}
		// var txt = "";
		// 	txt = "<li><a href="#!">"+data.versions+"</a></li>";
		// 	console.log(data[i].versions);
		
		// // Replace table’s tbody html with txt
		// $("#dropdown-mobile").html(txt);
		// $("#dropdown1").html(txt);
	}
});
