from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "wielsidljieleisleisl!"

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/registration', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")

    if len(request.form['first_name']) < 1:
        flash("First name cannot be blank!")

    if len(request.form['last_name']) < 1:
        flash("Last Name cannot be blank!")

    if len(request.form['password']) < 8:
        flash("Password must be more than 8 characters")

    if len(request.form['password']) < 1:
        flash("Password cannot be blank!")
    
    else:
        flash(f"Success! Your Registration has been submitted.")

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
