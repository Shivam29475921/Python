from flask import Flask, render_template, request
import requests
import smtplib
import ssl
GMAIL_SMTP_SERVER = "smtp.gmail.com"
PORT = 465
EMAIL = "shivamdas16122002@gmail.com"
PASSWORD = "wxdzfazvtfnjfwzm"
# PASSWORD = "M(S+8*N6#4weF&a7M&RD"
context = ssl.create_default_context()

response = requests.get("https://api.npoint.io/3af99b44bd26f7cb848a")
posts = response.json()
app = Flask(__name__, template_folder="templates")


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<int:index>')
def show_post(index):

    requested_post = None
    for post in posts:
        if post['id'] == index:
            requested_post = post
    return render_template("post.html", requested_post=requested_post)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return receive_data()
    return render_template("contact.html")


def receive_data():
    name = request.form['username']
    email = request.form['email']
    phone_number = request.form['phone_number']
    message = request.form['message']
    send_email(name, email, phone_number, message)
    return render_template("contact.html", message="Your message was sent successfully")


def send_email(name, email, phone_number, message):
    email_content = f"Subject:New Message from {name}({email})\n\n" \
                    f"{message}\n" \
                    f"Contact:{phone_number}"
    with smtplib.SMTP_SSL(GMAIL_SMTP_SERVER, PORT, context=context) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(from_addr=GMAIL_SMTP_SERVER, to_addrs=EMAIL, msg=email_content)


if __name__ == "__main__":
    app.run(debug=True)
