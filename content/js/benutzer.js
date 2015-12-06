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