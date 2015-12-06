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