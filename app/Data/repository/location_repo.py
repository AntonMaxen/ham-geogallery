import app.Data.repository.table_functions as tf
from app.Data.models.model_imports import *
from app.utils import print_dict, print_dicts


def get_all_locations():
    return tf.get_all_rows(Location)


def get_location_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Location, row_id)


def remove_location_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Location, row_id)


def add_location(row_dict):
    return tf.add_row(Location, row_dict)


def update_location(location_row, col_name, new_value):
    return tf.update_row_column(location_row, col_name, new_value)


def search_location(col_name, value):
    return tf.get_rows_like_column_value(Location, col_name, value)


if __name__ == '__main__':
    pass
