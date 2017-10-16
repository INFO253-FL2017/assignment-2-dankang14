var contactForm = document.getElementById("contact");
contactForm.addEventListener("submit", function(event) {

	var contactDiv = document.getElementById("react");
	contactDiv.innerHTML = localStorage.curlocation;

	contactDiv.classList.remove("error");
	contactDiv.classList.remove("send");

	event.preventDefault();

	var flname = document.getElementById("f&lname").value; 
	var subject = document.getElementById("subject").value;
	var message = document.getElementById("message").value;

	contactDiv.innerHTML = "You need to submit";
	if (flname.length == 0){
		contactDiv.innerHTML += " Your name";
	}  
	if (subject.length == 0) {
		contactDiv.innerHTML += "  Subject";
	} 
	if (message.length == 0) {
		contactDiv.innerHTML += "  Message";
	} 
	else{
		contactDiv.innerHTML= "Message sent, thanks";
	}
	if (contactDiv.innerHTML != "Message sent, thanks") {
		contactDiv.classList.add("send");
	} else {
		contactDiv.classList.add("error");
	}

})