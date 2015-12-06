function check_form(form_elem) {
	var schimpfwoerter = ['arsch', 'schlampe', 'scheiße', 'blödman'];

	if(form_elem.find('textarea, input').length > 0) {
		var elements = form_elem.find('textarea, input');

		elements.each(function() {
			for(var i in schimpfwoerter) {
				var regex = new RegExp(schimpfwoerter[i]);
				if(regex.test($(this).val())) {
					alert("Keine Schimpfwörter!");
					return false;
				}
			}
		});
	}

	return true;
}