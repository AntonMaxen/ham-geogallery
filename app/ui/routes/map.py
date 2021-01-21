from flask import Blueprint, render_template, url_for, request
import app.bl.location_controller as lc
import app.bl.utility_controller as uc
import json
from app.utils import make_list_of_dicts_jsonable
bp = Blueprint('map', __name__, url_prefix='/map')


@bp.route('/')
def index():
    locations = lc.get_all_locations()
    test_l = locations[1]
    print(test_l.picture)
    location_dicts = uc.rows_to_dicts(locations)
    location_dicts = make_list_of_dicts_jsonable(location_dicts)
    location_id = request.args.get('location_id')
    location_id = location_id if location_id else None
    jinja_dict = {
        'locations': location_dicts,
        'location_id': location_id
    }

    return render_template('map.html', **jinja_dict)


def test():
    location_dicts = uc.rows_to_dicts(lc.get_all_locations())
    print(make_list_of_dicts_jsonable(location_dicts))


if __name__ == '__main__':
    test()
