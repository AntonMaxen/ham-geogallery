import app.Data.repository.table_functions as tf
from app.Data.models.model_imports import *


def get_all_categories():
    return tf.get_all_rows(Category)


def get_category_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Category, row_id)


def remove_category_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Category, row_id)


def add_category(row_dict):
    return tf.add_row(Category, row_dict)


def update_category(category_row, col_name, new_value):
    return tf.update_row_column(category_row, col_name, new_value)


def search_category(col_name, value):
    return tf.get_rows_like_column_value(Category, col_name, value)


def get_parent_categories(category_row):
    if category_row is None:
        return []

    got_parent = True
    categories = []

    while got_parent:
        categories.append(category_row)
        parent_id = category_row.ParentId
        if parent_id:
            category_row = get_category_by_id(parent_id)
        else:
            got_parent = False

    return categories


if __name__ == '__main__':
    for row in get_all_categories():
        result = {col: getattr(row, col) for col in tf.get_columns(row)}
        print(result)

    ss = get_category_by_id(2)
    so = get_parent_categories(ss)
    print(so)
    for row in so:
        print(row.Name)

    for row in get_all_categories():
        result = {col: getattr(row, col) for col in tf.get_columns(row)}
        print(result)
