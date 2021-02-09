import datetime

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import app.bl.user_controller as uc

bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET'])
def login():
    print(current_user)
    if current_user.is_authenticated:
        return redirect('/map')
    else:
        return render_template('login.html')


@bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = bool(request.form.get('remember'))

    user = uc.get_user_by_email(email)

    if not user or not check_password_hash(user.Hash, password):
        flash('Please check your login details and try again.', 'danger')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    flash(f'Logged in as {user.Username}', 'success')
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

    if user:
        flash('Email address already exists.', 'danger')
        return redirect(url_for('auth.signup'))

    new_user = {
        'Email':email,
        'Username':username,
        'Hash': generate_password_hash(password, method='sha256', salt_length=32),
        'JoinDate': datetime.date.today(),
        'PermissionLevel': 1
    }
    flash('Signup successfull', 'success')

    uc.add_user(new_user)
    return redirect('/login')


@bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('Logging out', 'info')
    return redirect('/map')
