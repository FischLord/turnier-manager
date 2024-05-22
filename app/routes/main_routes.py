from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from . import main
from ..models.user import User

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Für eine echte Anwendung sollte das Passwort gehashed werden
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Ungültiger Benutzername oder Passwort', 'danger')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
