from flask import Blueprint, render_template, request
from flask_login import current_user
import app.bl.location_controller as lc
import app.bl.utility_controller as uc
from app.utils import make_list_of_dicts_jsonable, make_dict_jsonable
bp = Blueprint('map', __name__, url_prefix='/map')


@bp.route('/')
def index():
    locations = lc.get_all_locations()
    location_dicts = uc.rows_to_dicts(locations)
    location_dicts = make_list_of_dicts_jsonable(location_dicts)
    location_id = request.args.get('location_id')
    location_id = location_id if location_id else None
    jinja_dict = {
        'locations': location_dicts,
        'location_id': location_id,
    }
    if current_user.is_authenticated:
        print(current_user)
        user_dict = uc.row_to_dict(current_user)
        user_dict = make_dict_jsonable(user_dict)
        jinja_dict['user'] = user_dict

    return render_template('map.html', **jinja_dict)
