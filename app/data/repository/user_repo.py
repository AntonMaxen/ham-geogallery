import app.data.repository.table_functions as tf
from app.data.models.model_imports import *
from sqlalchemy import exc
from app.data.db import session
from app.utils import print_dict, print_dicts
import secrets


def get_all_users():
    return tf.get_all_rows(User)


def get_user_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(User, row_id)


def remove_user_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(User, row_id)


def remove_user_by_email(row_id):
    return tf.remove_row_by_id(User, row_id, col_name='Email')

def remove_user_by_username(username):
    return tf.remove_row_by_id(User, username, col_name='Username')


def get_user_by_username(username):
    return tf.get_row_by_column(User, username, col_name='Username')


def add_user(row_dict):
    return tf.add_row(User, row_dict)


def update_user(user_row, col_name, new_value):
    return tf.update_row_column(user_row, col_name, new_value)


def search_user(col_name, value):
    return tf.get_rows_like_column_value(User, col_name, value)


def add_user_token(user_row):
    token = generate_hex_token()
    result = search_user('Token', token)
    if len(result) <= 0:
        try:
            user_row.Token = token
            session.commit()
        except exc.SQLAlchemyError:
            session.rollback()
            return None

    return user_row


def get_user_by_token(token):
    return tf.get_row_by_column(User, token, col_name='Token')


def remove_user_token(user_row):
    try:
        user_row.Token = None
        session.commit()
    except exc.SQLAlchemyError:
        session.rollback()
        return None

    return user_row


def generate_hex_token(size=16):
    return secrets.token_hex(16)


if __name__ == '__main__':
    user = get_user_by_id(1)
    add_user_token(user)
    print(user.Token)
    print(user.Token)
