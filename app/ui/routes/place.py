from flask import Blueprint, render_template
import app.bl.location_controller as lc
import app.bl.utility_controller as uc
import app.bl.review_controller as rc
from app.data.db import *

bp = Blueprint('place', __name__, url_prefix='/place')
@bp.route('/')
def place():
    return render_template('place.html')


@bp.route('/<place_name>')
def place_name(place_name):
    # pictures
    # picture_like
    # reviews
    # comments
    # comment_likes
    # users

    locrev = session.query(lc.lr.Location).filter(lc.lr.Location.Place.like(f'%{place_name}%')).all()
    pic = []


    return render_template('place_name.html', place_name=place_name,locrev=locrev,pic=pic)


@bp.route('/<place_name>/<category_name>')
def place_name_category(place_name, category_name):
    pass


if __name__ == '__main__':
    pass
