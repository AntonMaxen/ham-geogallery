import app.Data.repository.table_functions as tf
from app.Data.models.model_imports import *
from app.utils import print_dict, print_dicts


def get_all_pictures():
    return tf.get_all_rows(Picture)


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


if __name__ == '__main__':
    pass
