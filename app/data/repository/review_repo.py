import app.data.repository.table_functions as tf
from app.data.models.model_imports import *


def get_all_reviews():
    return tf.get_all_rows(Review)


def get_review_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Review, row_id, 'UserId')


def get_review_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Review, row_id, 'Id')


def get_review_by_location_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Review, row_id, 'LocationId')


def remove_review_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Review, row_id)


def add_review(row_dict):
    return tf.add_row(Review, row_dict)


def update_review(review_row, col_name, new_value):
    return tf.update_row_column(review_row, col_name, new_value)
