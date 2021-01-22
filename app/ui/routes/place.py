from flask import Blueprint, render_template
import app.bl.location_controller as lc
import app.bl.utility_controller as uc
bp = Blueprint('place', __name__, url_prefix='/place')


@bp.route('/')
def place():
    return render_template('place.html')


@bp.route('/<place_name>')
def place_name(place_name):
    places = lc.get_location_by_place_name(place_name)
    # pictures
    # picture_like
    # reviews
    # comments
    # comment_likes
    # users

    place_dicts = uc.rows_to_dicts(places)
    return render_template('place_name.html', place_name=place_name,
                           places_dicts=place_dicts)


@bp.route('/<place_name>/<category_name>')
def place_name_category(place_name, category_name):
    pass


if __name__ == '__main__':
    pass
