$.ajax({
	type: "GET",
	url: "/getAvailableVersions",
	dataType: "json",
	success: function(data) {

		var txt = "";
		for (i= 0; i < data.versions.length; i++){
			 console.log(data.versions[i])
			 txt += "<li><a href='#!'>" + data.versions[i] + "</a></li>;"
		}
		
		// Replace table’s tbody html with txt
		$("#dropdown-mobile").html(txt);
		$("#dropdown1").html(txt);
	}
});
