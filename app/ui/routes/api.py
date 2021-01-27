from flask import Blueprint, render_template, url_for, request, send_file
import app.bl.location_controller as lc
import app.bl.utility_controller as uc
import app.bl.picture_controller as pc
import app.bl.picture_like_controller as plc
import app.bl.review_like_controller as rlc
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
    if locations is None:
        return json.dumps({
            'status': 404
        })

    location_dicts = uc.rows_to_dicts(locations)
    location_dicts = make_list_of_dicts_jsonable(location_dicts)
    return json.dumps(location_dicts)


@bp.route('/resource/location/<location_id>/picture/all')
def location_pictures_all(location_id):
    location = lc.get_location_by_id(location_id)
    if location is None:
        return json.dumps({
            'status': 404
        })

    pictures = location.picture
    picture_dicts = uc.rows_to_dicts(pictures)
    picture_dicts = make_list_of_dicts_jsonable(picture_dicts)
    return json.dumps(picture_dicts)


@bp.route('/resource/location/<location_id>/picture')
def location_picture(location_id):
    location = lc.get_location_by_id(location_id)
    if location is None:
        return json.dumps({
            'status': 404
        })

    amount = request.args.get('amount')
    amount = 1 if not amount or int(amount) < 1 else int(amount)
    pictures = location.picture[:amount]
    picture_dicts = uc.rows_to_dicts(pictures)
    picture_dicts = make_list_of_dicts_jsonable(picture_dicts)
    return json.dumps(picture_dicts)


@bp.route('/resource/location/<location_id>/review')
def location_review(location_id):
    location = lc.get_location_by_id(location_id)
    if location is None:
        return json.dumps({
            'status': 404
        })

    amount = request.args.get('amount')
    amount = 1 if not amount or int(amount) < 1 else int(amount)
    reviews = location.review[:amount]
    review_dicts = uc.rows_to_dicts(reviews)
    review_dicts = make_list_of_dicts_jsonable(review_dicts)
    return json.dumps(review_dicts)


@bp.route('/resource/location/<location_id>/review/all')
def location_reviews_all(location_id):
    location = lc.get_location_by_id(location_id)
    if location is None:
        return json.dumps({
            'status': 404
        })

    reviews = location.review
    review_dicts = uc.rows_to_dicts(reviews)
    review_dicts = make_list_of_dicts_jsonable(review_dicts)
    return json.dumps(review_dicts)


@bp.route('/resource/picture/<picture_id>/like/count')
def picture_likes(picture_id):
    amount_of_likes = plc.get_amount_of_likes_by_picture_id(picture_id)
    if amount_of_likes is None:
        amount_of_likes = {
            'status': 404
        }
    return json.dumps(amount_of_likes)


@bp.route('/resource/review/<review_id>/like/count')
def review_likes(review_id):
    amount_of_likes = rlc.get_amount_of_likes_by_review_id(review_id)
    if amount_of_likes is None:
        amount_of_likes = {
            'status': 404
        }

    return json.dumps(amount_of_likes)


@bp.route('/static/image/<file_name>')
def picture(file_name):
    image_folder = 'Photos'
    img_path = os.path.join(get_project_root(), image_folder, file_name)
    return send_file(img_path, mimetype='image/gif')


if __name__ == '__main__':
    pass
