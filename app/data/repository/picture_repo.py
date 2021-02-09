import app.data.repository.table_functions as tf
from app.data.models.model_imports import *


def get_all_pictures():
    return tf.get_all_rows(Picture)


def get_pictures_by_colname_desc_id(location_id, col_name='Id'):
    return tf.get_rows_by_column_order_by_desc(
        Picture,
        location_id,
        col_name=col_name,
        order_id='Id'
    )


def get_picture_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Picture, row_id)


def get_pictures_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_rows_by_column(Picture, row_id, col_name='UserId')


def get_pictures_by_location_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_rows_by_column(Picture, row_id, col_name='LocationId')


def remove_picture_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Picture, row_id)


def add_picture(row_dict):
    return tf.add_row(Picture, row_dict)


def update_picture(picture_row, col_name, new_value):
    return tf.update_row_column(picture_row, col_name, new_value)


def search_picture(col_name, value):
    return tf.get_rows_like_column_value(Picture, col_name, value)


def get_most_recent_row():
    return tf.get_highest_row(Picture)
