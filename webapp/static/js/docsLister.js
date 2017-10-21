$.ajax({
	type: "GET",
	url: "/getContent?filetype=doc",
	dataType: "json",
	success: function(data) {


		console.log(data[0])
		content = ''

		for(i = 0; i < data.length; i++ ){
			console.log(data[i].name)

			new_item = '<a href="/resources/'+ data[i].path +'"class="collection-item">'
			new_item += '<b>'+data[i].name+'</b>'

			if (data[i].description){
				new_item += ' - ' + data[i].description
				
			}

			new_item += '</a>'
			content += new_item
		}	

		$('#booksContainer').html(content)

	}
});
