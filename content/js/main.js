function sortByKuerzel() {
	var table1 = document.querySelector("table#sort-by-kuerzel");
	var table2 = document.querySelector("table#sort-by-semester");

	var button1 = document.querySelector("button#sort-by-kuerzel");
	var button2 = document.querySelector("button#sort-by-semester");

	table1.style.display = "table";
	table2.style.display = "none";

	button1.style.display = "";
	button2.style.display = "none";
}

function sortBySemester() {
	var table1 = document.querySelector("table#sort-by-kuerzel");
	var table2 = document.querySelector("table#sort-by-semester");

	var button1 = document.querySelector("button#sort-by-kuerzel");
	var button2 = document.querySelector("button#sort-by-semester");

	table1.style.display = "none";
	table2.style.display = "table";

	button2.style.display = "";
	button1.style.display = "none";
}