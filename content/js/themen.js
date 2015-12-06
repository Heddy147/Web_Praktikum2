function selectThema(element) {
	var elem = $(element);

	if(elem.hasClass("selected-thema")) {
		elem.removeClass("selected-thema");
		$("button").attr("disabled", "disabled");
	} else {
		$(".thema").removeClass("selected-thema");
		elem.addClass("selected-thema");
		$("button").removeAttr("disabled");
	}
}

function viewThema() {
	if($(".selected-thema").length > 0) {
		location.href = "/diskussionen/index/" + $(".selected-thema").data("id");
	}
}

function deleteThema() {
	if($(".selected-thema").length > 0) {
		location.href = "/themen/delete/" + $(".selected-thema").data("id");
	}
}

function editThema() {
	if($(".selected-thema").length > 0) {
		location.href = "/themen/edit/" + $(".selected-thema").data("id");
	}
}

$(document).ready(function() {
	$('#form-thema').submit(function(event) {
		event.preventDefault();
		var form_elem = $(this);

		if(check_form(form_elem)) {
			var daten = {};
			var method = "POST";

			form_elem.find('input').each(function() {
				daten[$(this).attr('name')] = $(this).val();
			});

			if(typeof form_elem.data('themen-id') != "undefined") {
				daten.id = form_elem.data('themen-id');
				method = "PUT";
			}

			$.ajax({
				method: method,
				url: "/api/themen",
				contentType: "plain/text",
				data: JSON.stringify(daten)
			}).done(function() {
				alert("Thema wurde gespeichert!");
				if(method == "POST") {
					form_elem.find('input').each(function() {
						$(this).val('');
					});
				}
			}).fail(function() {
				alert("Irgendwas ist schief gelaufen!")
			});
		}
	});
});