function selectUser(element) {
	var elem = $(element);

	if(elem.hasClass("selected-user")) {
		elem.removeClass("selected-user");
		$("button").attr("disabled", "disabled");
	} else {
		$(".user").removeClass("selected-user");
		elem.addClass("selected-user");
		$("button").removeAttr("disabled");
	}
}

function editUser() {
	if($(".selected-user").length > 0) {
		location.href = "/benutzer/edit/" + $(".selected-user").data("id");
	}
}

function deleteUser() {
	if($(".selected-user").length > 0) {
		location.href = "/benutzer/delete/" + $(".selected-user").data("id");
	}
}

$(document).ready(function() {
	$('#form-benutzer').submit(function(event) {
		event.preventDefault();
		var form_elem = $(this);

		var daten = {};
		var method = "POST";

		form_elem.find('input, textarea, select').each(function() {
			daten[$(this).attr('name')] = $(this).val();
		});

		if(typeof form_elem.data('benutzer-name') != "undefined") {
			daten.benutzername = form_elem.data('benutzer-name');
			method = "PUT";
		}

		$.ajax({
			method: method,
			url: "/api/benutzer",
			contentType: "plain/text",
			data: JSON.stringify(daten)
		}).done(function(data) {
			if(data == "false_not_logged_in") {
				alert("Sie sind nicht angemeldet!");
			} else if(data == "false_error") {
				alert("Es sind Fehler aufgetreten!");
			} else if(data == "false_rights") {
				alert("Sie haben nicht die nötigen Rechte!");
			} else {
				alert("Benutzer wurde gespeichert!");
				if(method == "POST") {
					form_elem.find('input, textarea, select').each(function() {
						$(this).val('');
					});
				}
			}
		}).fail(function() {
			alert("Es sind Fehler aufgetreten!")
		});
	});
});