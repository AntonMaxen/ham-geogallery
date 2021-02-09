from flask import Blueprint, render_template
import app.bl.location_controller as lc

bp = Blueprint('place', __name__, url_prefix='/place')


@bp.route('/')
def place():
    location = lc.get_location("")

    return render_template(
        'place_name.html', location=location)


@bp.route('/<name>')
def place_name(name):
    location = lc.get_location(name)

    return render_template(
        'place_name.html', location=location)
