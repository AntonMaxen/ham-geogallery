from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
import app.bl.utility_controller as uc
import json
import datetime
import app.bl.user_controller as user_c
from app.utils import make_dict_jsonable
bp = Blueprint('profile', __name__, url_prefix='/profile')


@bp.route('/')
@login_required
def index():
    print(current_user)
    user_dict = uc.row_to_dict(current_user)
    user_dict = make_dict_jsonable(user_dict)
    return render_template('profile.html', user=user_dict)
