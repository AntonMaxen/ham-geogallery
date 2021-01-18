import app.Data.repository.table_functions as tf
from app.Data.models.model_imports import *


def get_all_review_likes():
    return tf.get_all_rows(ReviewLike)


def get_review_like_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(ReviewLike, row_id, 'UserId')


def get_review_likes_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(ReviewLike, row_id, col_name='UserId')


def get_review_likes_by_review_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(ReviewLike, row_id, col_name='ReviewId')


def remove_review_like_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(ReviewLike, row_id)


def remove_review_likes_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_rows_by_column_name(
            ReviewLike,
            row_id,
            col_name='UserId'
        )


def remove_review_likes_by_review_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_rows_by_column_name(
            CommentLike,
            row_id,
            col_name='ReviewId'
        )


def add_review_like(row_dict):
    return tf.add_row(ReviewLike, row_dict)


def update_review_like(review_like_row, col_name, new_value):
    return tf.update_row_column(review_like_row, col_name, new_value)


def search_review_like(col_name, value):
    return tf.get_rows_like_column_value(ReviewLike, col_name, value)
