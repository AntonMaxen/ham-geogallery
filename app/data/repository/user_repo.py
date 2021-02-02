import app.data.repository.table_functions as tf
from app.data.models.model_imports import *
from app.utils import print_dict, print_dicts


def get_all_users():
    return tf.get_all_rows(User)


def get_user_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(User, row_id)


def remove_user_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(User, row_id)


def add_user(row_dict):
    return tf.add_row(User, row_dict)


def update_user(user_row, col_name, new_value):
    return tf.update_row_column(user_row, col_name, new_value)


def search_user(col_name, value):
    return tf.get_rows_like_column_value(User, col_name, value)


if __name__ == '__main__':
    for u in [tf.row_to_dict(user) for user in get_all_users()]:
        pass
        # print_dict(u)

    dicts = tf.rows_to_dicts(search_user('FirstName', "Allison"))
    print_dicts(dicts)
