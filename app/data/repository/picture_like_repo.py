import app.data.repository.table_functions as tf
from app.data.models.model_imports import *


def get_all_pic_likes():
    return tf.get_all_rows(PictureLike)


def get_pic_like_by_picture_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(PictureLike, row_id, 'PictureId')


def get_pic_like_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(PictureLike, row_id, 'UserId')


def add_pic_like(row_dict):
    return tf.add_row(PictureLike, row_dict)


def update_pic_like(picture_like_row, col_name, new_value):
    return tf.update_row_column(picture_like_row, col_name, new_value)


def get_liked_pictures(pic_id):
    tf.get_row_by_column(PictureLike, 'Picture_id', pic_id)


def get_user_that_liked_pictures(pic_id):
    tf.get_row_by_column(PictureLike, 'User_id', pic_id)


def unlike_by_picture_id(row_id):
    tf.remove_row_by_id(PictureLike, row_id, 'PictureId')


def unlike_by_user_id(row_id):
    tf.remove_row_by_id(PictureLike, row_id, 'UserId')
