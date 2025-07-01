from flask import render_template, request, redirect, url_for, flash
from mod import app, db
from mod.models import User
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        action = request.form.get("action")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if action == "register":
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash("Email already registered!", "danger")
            else:
                hashed_password = generate_password_hash(password)
                new_user = User(username=username, email=email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash("Registration successful! Please log in.", "success")
        
        elif action == "login":
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                flash("Login successful!", "success")
                return redirect(url_for("home"))
            else:
                flash("Invalid credentials.", "danger")

    return render_template("frontend_login_signup.html")
