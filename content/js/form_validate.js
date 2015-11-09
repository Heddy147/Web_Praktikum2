$(document).ready(function() {
	$('form').submit(check_form);
});

function check_form(event) {
	var schimpfwoerter = ['arsch', 'schlampe', 'blödmann', 'scheiße', 'blödman'];

	if($('form textarea[name="text"]').length == 1) {
		var input_value = $('form textarea[name="text"]').val();
		for(var i in schimpfwoerter) {
			var regex = new RegExp(schimpfwoerter[i]);
			if(regex.test(input_value)) {
				alert("Keine Schimpfwörter!");
				event.preventDefault();
			}
		}
	}
}