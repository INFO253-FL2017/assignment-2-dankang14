1. What is the function of the following technologies in your assignment:
	HTML:
		includes codes that structures the website in a certain way based on the way we write it. 
	CSS:
		styles the website by modifiying the HTML elements in order to give the website a type of design. (i.e. changing the color, font size, or location of the headings) 
	JavaScript:
		a language that is used in order to run the contact forms 
	Python:
		the program in language. 
	Flask:
		a type of framework 
	HTTP:
		connection between server and web 
	GET and POST requests:
		GET requests information from the server
		POST gets information and sends it to the server(MAILGUN) 

2. How does HTML, CSS, and JavaScript work together in the browser for this assignment?
	HTML sets up the layout, CSS decorates it, and JavaScript implement the program.

3. How does Python and Flask work together in the server for this assignment?
	Through python, Flask gathers information and runs the server on the local and is thus powered by python.


4. List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request
GET:/
	renders the index.html template file
GET: /index
	renders the index.html template file
GET: /contact
	renders the contact.html template file
GET: /about
	renders the about.html template file
GET: /blog/(title)
	renders each blogs in blog folder
POST: /contact
	submit the form information as an email to the MAILGUN api and also renders the contact.html