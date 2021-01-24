from flask import Blueprint, render_template, url_for, request, send_file
import app.bl.location_controller as lc
import app.bl.utility_controller as uc
import app.bl.picture_controller as pc
from app.utils import (
    make_list_of_dicts_jsonable,
    make_dict_jsonable,
    get_project_root
)
import os
import json
bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/resource/location/all')
def all_locations():
    locations = lc.get_all_locations()
    location_dicts = uc.rows_to_dicts(locations)
    location_dicts = make_list_of_dicts_jsonable(location_dicts)
    return json.dumps(location_dicts)


@bp.route('/resource/location/<location_id>/picture/all')
def location_pictures(location_id):
    location = lc.get_location_by_id(location_id)
    pictures = location.picture
    picture_dicts = uc.rows_to_dicts(pictures)
    picture_dicts = make_list_of_dicts_jsonable(picture_dicts)
    return json.dumps(picture_dicts)


@bp.route('/resource/location/<location_id>/review/all')
def location_reviews(location_id):
    location = lc.get_location_by_id(location_id)
    reviews = location.review
    review_dicts = uc.rows_to_dicts(reviews)
    review_dicts = make_list_of_dicts_jsonable(review_dicts)
    return json.dumps(review_dicts)


@bp.route('/static/image/<file_name>')
def picture(file_name):
    image_folder = 'Photos'
    img_path = os.path.join(get_project_root(), image_folder, file_name)
    return send_file(img_path, mimetype='image/gif')


if __name__ == '__main__':
    pass
