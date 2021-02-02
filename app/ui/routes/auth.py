import datetime
import random

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.data.models.user import User
import app.bl.user_controller as uc

bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = bool(request.form.get('remember'))

    user = uc.get_user_by_email(email)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.Hash, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect('/map')


@bp.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@bp.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('Email')
    username = request.form.get('Username')
    password = request.form.get('Password')

    user = uc.get_user_by_email(email)

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = {
        'Email':email,
        'Username':username,
        'Hash': generate_password_hash(password, method='sha256', salt_length=32),
        'JoinDate': datetime.date.today(),
        'PermissionLevel': 1
    }

    uc.add_user(new_user)
    return redirect('/login')


@bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect('/map')
