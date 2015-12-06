function selectBeitrag(element) {
	var elem = $(element);

	if(elem.hasClass("selected-beitrag")) {
		elem.removeClass("selected-beitrag");
		$("button").attr("disabled", "disabled");
	} else {
		$(".beitrag").removeClass("selected-beitrag");
		elem.addClass("selected-beitrag");
		$("button").removeAttr("disabled");
	}
}

function deleteBeitrag(diskussions_id) {
	if($(".selected-beitrag").length > 0) {
		location.href = "/beitraege/delete/" + diskussions_id + "/" + $(".selected-beitrag").data("id");
	}
}

function editBeitrag(diskussions_id) {
	if($(".selected-beitrag").length > 0) {
		location.href = "/beitraege/edit/" + diskussions_id + "/" + $(".selected-beitrag").data("id");
	}
}

$(document).ready(function() {
	$('#form-beitrag').submit(function(event) {
		event.preventDefault();
		var form_elem = $(this);

		if(check_form(form_elem)) {
			var daten = {};
			var method = "POST";

			form_elem.find('input, textarea').each(function() {
				daten[$(this).attr('name')] = $(this).val();
			});

			if(typeof form_elem.data('beitrags-id') != "undefined") {
				daten.id = form_elem.data('beitrags-id');
				method = "PUT";
			}

			$.ajax({
				method: method,
				url: "/api/beitraege/" + form_elem.data('diskussions-id'),
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
					alert("Beitrag wurde gespeichert!");
					if(method == "POST") {
						form_elem.find('input, textarea').each(function() {
							$(this).val('');
						});
					}
				}
			}).fail(function() {
				alert("Es sind Fehler aufgetreten!")
			});
		}
	});
});