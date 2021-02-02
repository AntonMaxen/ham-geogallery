from flask import Blueprint, render_template
from flask_login import login_required, current_user
import app.bl.utility_controller as uc
import json
from app.utils import make_dict_jsonable
bp = Blueprint('profile', __name__, url_prefix='/profile')


@bp.route('/')
@login_required
def index():
    user_dict = uc.row_to_dict(current_user)
    user_dict = make_dict_jsonable(user_dict)
    return json.dumps(user_dict)

