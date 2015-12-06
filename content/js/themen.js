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
	$('#form-create-thema').submit(function(event) {
		event.preventDefault();
		var form_elem = $(this);

		if(check_form(form_elem)) {
			var daten = {};

			form_elem.find('input').each(function() {
				daten[$(this).attr('name')] = $(this).val();
			});

			$.ajax({
				method: "POST",
				url: "/api/themen",
				contentType: "plain/text",
				data: JSON.stringify(daten)
			}).done(function() {
				alert("Thema wurde gespeichert!");
				form_elem.find('input').each(function() {
					$(this).val('');
				});
			}).fail(function() {
				alert("Irgendwas ist schief gelaufen!")
			});
		}
	});
});