function selectDiskussion(element) {
	var elem = $(element);

	if(elem.hasClass("selected-diskussion")) {
		elem.removeClass("selected-diskussion");
		$("button").attr("disabled", "disabled");
	} else {
		$(".diskussion").removeClass("selected-diskussion");
		elem.addClass("selected-diskussion");
		$("button").removeAttr("disabled");
	}
}

function viewDiskussion() {
	if($(".selected-diskussion").length > 0) {
		location.href = "/beitraege/index/" + $(".selected-diskussion").data("id");
	}
}

function deleteDiskussion(themen_id) {
	if($(".selected-diskussion").length > 0) {
		location.href = "/diskussionen/delete/" + themen_id + "/" + $(".selected-diskussion").data("id");
	}
}

function editDiskussion(themen_id) {
	if($(".selected-diskussion").length > 0) {
		location.href = "/diskussionen/edit/" + themen_id + "/" + $(".selected-diskussion").data("id");
	}
}

$(document).ready(function() {
	$('#form-diskussion').submit(function(event) {
		event.preventDefault();
		var form_elem = $(this);

		if(check_form(form_elem)) {
			var daten = {};
			var method = "POST";

			form_elem.find('input').each(function() {
				daten[$(this).attr('name')] = $(this).val();
			});

			if(typeof form_elem.data('diskussions-id') != "undefined") {
				daten.id = form_elem.data('diskussions-id');
				method = "PUT";
			}

			$.ajax({
				method: method,
				url: "/api/diskussionen/" + form_elem.data('themen-id'),
				contentType: "plain/text",
				data: JSON.stringify(daten)
			}).done(function(data) {
				if(data == "false_error") {
					alert("Es sind Fehler aufgetreten!");
				} else if(data == "false_not_admin") {
					alert("Sie haben nicht die noetigen Rechte!");
				} else {
					alert("Beitrag wurde gespeichert!");
					if(method == "POST") {
						form_elem.find('input').each(function() {
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