import requests
import os

"""
webserver.py
File that is the central location of code for your webserver.
"""

from flask import Flask, request, render_template
app = Flask(__name__,static_url_path="/static")


@app.route('/', methods=['GET'])
def default():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template('index.html')
@app.route('/index', methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
@app.route('/contact', methods=['GET'])
def conatct():
    return render_template('contact.html', notifications=[])
@app.route('/blog/8-experiments-in-motivation', methods=['GET'])
def blog_1():
    return render_template('/blog/8-experiments-in-motivation.html')
@app.route('/blog/a-mindful-shift-of-focus', methods=['GET'])
def blog_2():
    return render_template('/blog/a-mindful-shift-of-focus.html')
@app.route('/blog/how-to-develop-an-awesome-sense-of-direction', methods=['GET'])
def blog_3():
    return render_template('/blog/how-to-develop-an-awesome-sense-of-direction.html')
@app.route('/blog/training-to-be-a-good-writer', methods=['GET'])
def blog_4():
    return render_template('/blog/training-to-be-a-good-writer.html')
@app.route('/blog/what-productivity-systems-wont-solve', methods=['GET'])
def blog_5():
    return render_template('/blog/what-productivity-systems-wont-solve.html')

@app.route('/contact', methods=['POST'])
def send_email():
 message = request.form.get("message")
 name = request.form.get("f&lname")
 subject = request.form.get("subject")
 email = "Name: " + name + "Subject: " + subject + "Message: " + message
 notifications = []

 data = {
        'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
        'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
        'subject': subject,
        'text': email
    }
 auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

 r = requests.post(
        'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
        auth=auth,
        data=data)

 if r.status_code == requests.codes.ok:
        notifications.append("Hi" + name + "Your email was sent")
 else:
        notifications.append("You email was not sent. Please try again later")

 return render_template("contact.html", notifications=notifications)