import app.data.repository.table_functions as tf
from app.data.models.model_imports import *


def get_all_comments():
    return tf.get_all_rows(Comment)


def get_comment_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Comment, row_id, 'UserId')


def get_comment_by_review_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Comment, row_id, 'ReviewId')


def get_comment_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(Comment, row_id, 'Id')


def remove_comment_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Comment, row_id, 'UserId')


def remove_comment_by_review_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(Comment, row_id, 'ReviewId')


def add_comment(row_dict):
    return tf.add_row(Comment, row_dict)


def edit_comment(comment_row, new_value):
    return tf.update_row_column(comment_row, 'CommentText', new_value)
