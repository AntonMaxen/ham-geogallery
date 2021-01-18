import app.data.repository.table_functions as tf
from app.data.models.model_imports import *


def get_all_visited_location():
    return tf.get_all_rows(VisitedLocation)


def get_visited_location_by_location_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(VisitedLocation, row_id, "LocationId")


def get_visited_location_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(VisitedLocation, row_id, "UserId")


def remove_visited_location_by_location_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(VisitedLocation, row_id, "LocationId")


def remove_visited_location_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(VisitedLocation, row_id, "UserId")


def add_visited_location(row_dict):
    return tf.add_row(VisitedLocation, row_dict)


def update_visited_location(visited_location_row, col_name, new_value):
    return tf.update_row_column(visited_location_row, col_name, new_value)


def search_visited_location(col_name, value):
    return tf.get_rows_like_column_value(VisitedLocation, col_name, value)
