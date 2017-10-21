$.ajax({
	type: "GET",
	url: "/getContent?filetype=video",
	dataType: "json",
	success: function(data) {


		console.log(data[0])
		content = ''

		for(i = 0; i < data.length; i++ ){
			console.log(data[i].name)
			new_item = '<li class="collection-item avatar"><video class="responsive-video" controls>'
			new_item += '<source src="/resources/'+data[i].path+'"></video>'
			new_item += '<p><b>'+data[i].name+'</b><br>'
			
			if (data[i].description){
				new_item += data[i].description
				
			}
			new_item += '</p></li>'
			content += new_item
			console.log(new_item)
		}	
		console.log(content)

		$('#moviesContainer').html(content)

	}
});
