from flask import Blueprint, render_template
import app.bl.location_controller as lc
from app.data.db import *

bp = Blueprint('place', __name__, url_prefix='/place')


@bp.route('/')
def place():
    return render_template('place.html')


@bp.route('/<place_name>')
def place_name(place_name):
    location = lc.get_location(place_name)

    return render_template(
        'place_name.html', place_name=place_name, location=location)
