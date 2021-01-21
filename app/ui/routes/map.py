from flask import Blueprint, render_template, url_for, request
import app.bl.location_controller as lc
import app.bl.utility_controller as uc
import decimal
import json
bp = Blueprint('map', __name__, url_prefix='/map')


@bp.route('/')
def index():
    locations = lc.get_all_locations()
    location_dicts = uc.rows_to_dict(locations)
    location_dicts = make_list_of_dicts_jsonable(location_dicts)
    location_id = request.args.get('location_id')
    location_id = location_id if location_id else None
    jinja_dict = {
        'locations': location_dicts,
        'location_id': location_id
    }

    return render_template('map.html', **jinja_dict)


@bp.route('/all_locations.json')
def all_locations():
    locations = lc.get_all_locations()
    location_dicts = uc.rows_to_dict(locations)
    location_dicts = make_list_of_dicts_jsonable(location_dicts)
    return json.dumps(location_dicts)


def make_list_of_dicts_jsonable(list_of_dicts):
    return [make_dict_jsonable(my_dict) for my_dict in list_of_dicts]


def make_dict_jsonable(my_dict):
    return {k: float(str(v)) if isinstance(v, decimal.Decimal) else v
            for k, v in my_dict.items()}


def test():
    location_dicts = uc.rows_to_dict(lc.get_all_locations())
    print(make_list_of_dicts_jsonable(location_dicts))


if __name__ == '__main__':
    test()