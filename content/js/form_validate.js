$(document).ready(function() {
	$('form').submit(check_form);
});

function check_form(event) {
	var schimpfwoerter = ['arsch', 'schlampe', 'blödmann', 'scheiße', 'blödman'];

	if($('form textarea[name="text"]').length == 1 || $('form input[name="titel"]').length == 1) {
		var text_input_value = false;
		var titel_input_value = false;
		if($('form textarea[name="text"]').length == 1) {
			text_input_value = $('form textarea[name="text"]').val();
		}

		if($('form input[name="titel"]').length == 1) {
			text_input_value = $('form input[name="titel"]').val();
		}

		for(var i in schimpfwoerter) {
			var regex = new RegExp(schimpfwoerter[i]);
			if(text_input_value !== false && regex.test(text_input_value)) {
				alert("Keine Schimpfwörter!");
				event.preventDefault();
			}

			if(titel_input_value !== false && regex.test(titel_input_value)) {
				alert("Keine Schimpfwörter!");
				event.preventDefault();
			}
		}
	}
}