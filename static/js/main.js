function selectText(cid) {
	if (document.selection) { // IE
		var range = document.body.createTextRange();
		range.moveToElementText(document.getElementById(cid));
		range.select();
		document.execCommand("copy");
	} else if (window.getSelection) {
		var range= document.createRange();
		range.selectNode(document.getElementById(cid));
		window.getSelection().removeAllRanges();
		window.getSelection().addRange(range);
		document.execCommand("copy");
	}
}
function checkPops(id) {
	var x = document.getElementsByClassName("popup");
	for(i=0; i < x.length; i++) {
		if (i == id) {
			continue;
		}
		x[i].classList.add("nonactive");
	}
}

function toText() {
	var btn = document.getElementsByClassName("button_orng")[0];
	document.getElementsByClassName("soup_bowl")[0].className = "textonly";
	btn.innerHTML = "Change To Bubble Display";
	btn.removeEventListener("click", toText);
	btn.addEventListener("click", toBub);
}

function toBub() {
	var btn = document.getElementsByClassName("button_orng")[0];
	document.getElementsByClassName("textonly")[0].className = "soup_bowl";
	btn.innerHTML = "Change To Text Only";
	btn.removeEventListener("click", toBub);
	btn.addEventListener("click", toText);
}

function textSpeech() {
	if (window.localStorage.getItem('favObject')) {
		var favList = JSON.parse(window.localStorage.getItem('favObject'));
		for (i=0; i < favList.length; i ++) {
			var ediv = document.createElement("DIV");
			ediv.className = "fav";
			var elem = document.createElement("IMG");
			elem.src = favList[i]['img'];
			var elem1 = document.createElement("A");
			elem1.innerHTML = favList[i]['name'];
			var elem2 = document.createElement("A");
			elem2.innerHTML = favList[i]['url'];
			elem2.href = favList[i]['url'];
			ediv.appendChild(elem);
			ediv.appendChild(elem1);
			ediv.appendChild(elem2);
			document.getElementsByClassName("favs")[0].appendChild(ediv);
		}
	}
	if ('speechSynthesis' in window) {
		var synthesis = window.speechSynthesis;

		var voice = synthesis.getVoices().filter(function(voice){
			return voice.lang === 'en';
		})[0];

		document.getElementById("ingredVoice").addEventListener("click", function() {
			speechSynthesis.cancel();
			var ingred = document.getElementsByClassName("ingredients")[0].getElementsByTagName("UL")[0].getElementsByTagName("LI");

			for (i=0; i < ingred.length; i++) {
				var utterance = new SpeechSynthesisUtterance(ingred[i].innerHTML);
				utterance.voice = voice;
				utterance.voiceURI = 'native';
				utterance.pitch = 1;
				utterance.rate = 1;
				utterance.volume = 0.8;

				synthesis.speak(utterance);
			}
		});

		document.getElementById("dirVoice").addEventListener("click", function() {
			speechSynthesis.cancel();
			var dir = document.getElementsByClassName("directions")[0].getElementsByTagName("OL")[0].getElementsByTagName("LI");

			for (i=0; i < dir.length; i++) {
				var strsplit = dir[i].innerHTML.split(".");
				for (q=0; q < strsplit.length; q++) {
					if (strsplit[q].length > 0) {

						var utterance = new SpeechSynthesisUtterance(strsplit[q]);
						utterance.voice = voice;
						utterance.voiceURI = 'native';
						utterance.pitch = 1;
						utterance.rate = 1;
						utterance.volume = 0.8;

						synthesis.speak(utterance);
					}
				}

			}
		});

	} else {
		console.log('Text-to-speech not supported');
	}
}

function toggleFav(on) {
	if (on) {
		document.getElementsByClassName("favadd")[0].children[0].children[0].src = "/static/star.png";
		if (window.localStorage.getItem('favObject')) {
			var favList = JSON.parse(window.localStorage.getItem('favObject'));
		} else {
			var favList = [];
		}
		var favObject = {'img':document.getElementsByClassName("soup_img_cont")[0].children[0].src, 'name':document.getElementsByClassName("soup_img_cont")[0].children[1].innerHTML, 'url':document.getElementById('selectable2').innerHTML};
		favList.push(favObject);
		window.localStorage.setItem('favObject', JSON.stringify(favList));
		var ediv = document.createElement("DIV");
		ediv.className = "fav";
		var elem = document.createElement("IMG");
		elem.src = favObject['img'];
		var elem1 = document.createElement("A");
		elem1.innerHTML = favObject['name'];
		var elem2 = document.createElement("A");
		elem2.innerHTML = favObject['url'];
		elem2.href = favObject['url'];
		elem2.target = "_blank";
		ediv.appendChild(elem);
		ediv.appendChild(elem1);
		ediv.appendChild(elem2);
		document.getElementsByClassName("favs")[0].appendChild(ediv);
	} else {
		document.getElementsByClassName("favadd")[0].children[0].children[0].src = "/static/starw.png";
		var favList = JSON.parse(window.localStorage.getItem('favObject'));
		favList.pop();
		if (favList.length > 0) {
			window.localStorage.setItem('favObject', JSON.stringify(favList));
		} else {
			window.localStorage.removeItem('favObject');
		}
		document.getElementsByClassName("favs")[0].lastChild.remove();
	}
	console.log(window.localStorage);
}

function onChange(checkbox, xfunc) {
	const value = checkbox.nextElementSibling.checked;
	xfunc(value);
}

function toggleFavOpen(on) {
	var docadd = document.getElementsByClassName("favs")[0];
	if (on) {
		docadd.style.display = "block";
	} else {
		docadd.style.display = "none";
	}
}

/*
var interval = 1000;
var expected = Date.now() + interval;
setTimeout(step, interval);
function step() {
	var dt = Date.now() - expected;
	if (dt > interval) {
		console.log("MegaOOPS");
	}
	console.log("nice");

	expected += interval;
	setTimeout(step, Math.max(0, interval-dt));
}
*/
