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
	$('#form-create-beitrag').submit(function(event) {
		event.preventDefault();
		var form_elem = $(this);

		if(check_form(form_elem)) {
			var daten = {};

			form_elem.find('input, textarea').each(function() {
				daten[$(this).attr('name')] = $(this).val();
			});

			$.ajax({
				method: "POST",
				url: "/api/beitraege/" + form_elem.data('diskussions-id'),
				contentType: "plain/text",
				data: JSON.stringify(daten)
			}).done(function() {
				alert("Beitrag wurde gespeichert!");
				form_elem.find('input, textarea').each(function() {
					$(this).val('');
				});
			}).fail(function() {
				alert("Irgendwas ist schief gelaufen!")
			});
		}
	});
});