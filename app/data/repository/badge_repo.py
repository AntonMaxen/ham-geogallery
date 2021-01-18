import app.data.repository.table_functions as tf
from app.data.models.model_imports import *


def get_all_badges():
    return tf.get_all_rows(Badge)


def get_badge_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Badge, row_id, 'Id')


def add_badge(row_dict):
    return tf.add_row(Badge, row_dict)


def remove_badge(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Badge, row_id)


def update_badge_row(badge_row, col_name, new_value):
    return tf.update_row_column(badge_row, col_name, new_value)
