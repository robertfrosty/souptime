function mobileSearch(on) {
	if (on) {
		document.getElementsByClassName("mobile_search")[0].style.display = "block";
		document.getElementsByClassName("title")[0].style.display = "none";
	} else {
		document.getElementsByClassName("mobile_search")[0].style.display = "none";
		document.getElementsByClassName("title")[0].style.display = "flex";
	}
}
