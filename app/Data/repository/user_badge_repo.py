import app.Data.repository.table_functions as tf
from app.Data.models.model_imports import *


def get_all_user_badge():
    return tf.get_all_rows(UserBadge)


def get_user_badge_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(UserBadge, row_id, "UserId")


def get_user_badge_by_badge_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(UserBadge, row_id, "BadgeId")


def remove_user_badge_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Category, row_id, "UserId")


def remove_user_badge_by_badge_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Category, row_id, "BadgeId")


def add_user_badge(row_dict):
    return tf.add_row(UserBadge, row_dict)


def update_user_badge(category_row, col_name, new_value):
    return tf.update_row_column(category_row, col_name, new_value)


def search_user_badge(col_name, value):
    return tf.get_rows_like_column_value(UserBadge, col_name, value)
