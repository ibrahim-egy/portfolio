import smtplib
from flask import Flask, render_template, request
from datetime import datetime

MY_EMAIL = "pythontest1164@gmail.com"
MY_PASSWORD = "pythontester0#"

date = datetime.now()
year = date.strftime("%Y")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        send_email(name=name, email=email, message=message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=120) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=email, to_addrs=MY_EMAIL, msg=email_message)


if __name__ == '__main__':
    app.run(debug=True)
