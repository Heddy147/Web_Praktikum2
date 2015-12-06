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