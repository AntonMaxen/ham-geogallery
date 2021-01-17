import app.Data.repository.table_functions as tf
from app.Data.models.model_imports import *
from app.utils import print_dict, print_dicts


def get_all_locations():
    return tf.get_all_rows(Location)


def get_location_by_id(row_id):
    if tf.validate_number(row_id):
        rows = tf.get_row_by_column(Location, row_id)
        return rows[0] if len(rows) > 0 else rows


def get_locations_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Location, row_id, col_name='UserId')


def get_locations_by_category_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Location, row_id, col_name='CategoryId')


def remove_location_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Location, row_id)


def remove_locations_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_rows_by_column_name(
            Location,
            row_id,
            col_name='UserId'
        )


def remove_locations_by_category_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_rows_by_column_name(
            Location,
            row_id,
            col_name='CategoryId'
        )


def add_location(row_dict):
    return tf.add_row(Location, row_dict)


def update_location(location_row, col_name, new_value):
    return tf.update_row_column(location_row, col_name, new_value)


def search_location(col_name, value):
    return tf.get_rows_like_column_value(Location, col_name, value)


if __name__ == '__main__':
    remove_locations_by_user_id(6)
