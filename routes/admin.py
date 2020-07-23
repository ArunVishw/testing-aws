
from flask import Flask, render_template, url_for, redirect, request, session, flash, Blueprint
from routes.db import db, users
admin = Blueprint("admin", __name__, static_folder="../static", template_folder="../templates")

@admin.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if "email" in session:
        return render_template("dashboard.html",data=session)
    else:
        flash("Log In | Sign Up First", "alert")
        return redirect(url_for("admin.authenticate"))
    
@admin.route("/", methods=["POST","GET"])
@admin.route("/authenticate", methods=["POST","GET"])
def authenticate():
    if request.method == "POST":
        session.permanent = True
        if "name" in request.form:
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            confirm_password = request.form["confirm_password"]
            found_user = users.query.filter_by(email=email).first()
            if found_user:
                flash("Email already registered", "alert")
                return redirect(url_for("admin.authenticate"))
            elif password != confirm_password:
                flash("Password does not match", "alert")
                return redirect(url_for("admin.authenticate"))
            else:
                user = users(name=name, email=email, password=password)
                db.session.add(user)
                db.session.commit()
                session["email"] = email
                flash("Registered Successfully", "alert")
                return redirect(url_for("admin.dashboard"))
        else:
            email = request.form["email"]
            password = request.form["password"]
            found_user = users.query.filter_by(email=email, password=password).first()
            if found_user:
                session["email"] = email
                flash("Logged in sucessfully", "alert")
                return redirect(url_for("admin.dashboard"))
            else:
                flash("Invalid Credentials", "alert")
                return redirect(url_for("admin.authenticate"))
    else:
        return render_template("authenticate.html")

@admin.route("/logout", methods=["POST"])
def logout():
    session.pop("email",None)
    flash("You have been logged out", "alert")
    return redirect(url_for("admin.authenticate"))