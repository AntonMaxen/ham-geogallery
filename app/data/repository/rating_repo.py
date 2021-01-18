import app.data.repository.table_functions as tf
from app.data.models.model_imports import *


def get_all_rating():
    return tf.get_all_rows(Rating)


def get_rating_by_location_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Rating, row_id, "LocationId")


def get_rating_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Rating, row_id, "UserId")


def remove_rating_by_location_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Rating, row_id, "LocationId")


def remove_rating_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Rating, row_id, "UserId")


def add_rating(row_dict):
    return tf.add_row(Rating, row_dict)


def update_rating(rating_row, col_name, new_value):
    return tf.update_row_column(rating_row, col_name, new_value)


def search_rating(col_name, value):
    return tf.get_rows_like_column_value(Rating, col_name, value)
