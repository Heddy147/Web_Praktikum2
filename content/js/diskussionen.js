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