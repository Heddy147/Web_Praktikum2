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