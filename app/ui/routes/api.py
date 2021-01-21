from flask import Blueprint, render_template, url_for, request
import app.bl.location_controller as lc
import app.bl.utility_controller as uc
import app.bl.picture_controller as pc
from app.utils import make_list_of_dicts_jsonable, make_dict_jsonable
import json
bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/location/all')
def all_locations():
    locations = lc.get_all_locations()
    location_dicts = uc.rows_to_dicts(locations)
    location_dicts = make_list_of_dicts_jsonable(location_dicts)
    return json.dumps(location_dicts)


@bp.route('/location/<location_id>/picture/all')
def location_pictures(location_id):
    location = lc.get_location_by_id(location_id)
    pictures = location.picture
    picture_dicts = uc.rows_to_dicts(pictures)
    picture_dicts = make_list_of_dicts_jsonable(picture_dicts)
    return json.dumps(picture_dicts)


if __name__ == '__main__':
    pass
