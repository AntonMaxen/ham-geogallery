import app.data.repository.table_functions as tf
from app.data.models.model_imports import *
from app.data.db import *


def get_locations(place_name):
    return session.query(Location).\
        filter(Location.Place.like(f'%{place_name}%')).all()


def get_all_locations():
    return tf.get_all_rows(Location)


def get_location_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Location, row_id)


def get_locations_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_rows_by_column(Location, row_id, col_name='UserId')


def get_locations_by_category_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_rows_by_column(Location, row_id, col_name='CategoryId')


def remove_location_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Location, row_id)


def remove_locations_by_place_name(place_name):
    return tf.remove_rows_by_column_name(
        Location,
        place_name,
        col_name='Place'
    )


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
