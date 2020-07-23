const inputs = document.querySelectorAll(".input");


function addcl(){
	let parent = this.parentNode.parentNode;
	parent.classList.add("focus");
}

function remcl(){
	let parent = this.parentNode.parentNode;
	if(this.value == ""){
		parent.classList.remove("focus");
	}
}


inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
});

document.getElementById("register-link").onclick = function() {
	document.getElementById("login").style.display = "none";
	document.getElementById("register").style.display = "flex";
}

document.getElementById("login-link").onclick = function () {
	document.getElementById("register").style.display = "none";
	document.getElementById("login").style.display = "flex";
}
