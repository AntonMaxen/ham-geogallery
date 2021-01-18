import app.Data.repository.table_functions as tf
from app.Data.models.model_imports import *
from app.utils import print_dict, print_dicts


def get_all_comment_likes():
    return tf.get_all_rows(CommentLike)


def get_comment_like_by_id(row_id):
    if tf.validate_number(row_id):
        rows = tf.get_row_by_column(CommentLike, row_id)
        return rows[0] if len(rows) > 0 else rows


def get_comment_likes_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(CommentLike, row_id, col_name='UserId')


def get_comment_likes_by_comment_id(row_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(CommentLike, row_id, col_name='CommentId')


def remove_comment_like_by_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_row_by_id(CommentLike, row_id)


def remove_comment_likes_by_user_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_rows_by_column_name(
            CommentLike,
            row_id,
            col_name='UserId'
        )


def remove_comment_likes_by_comment_id(row_id):
    if tf.validate_number(row_id):
        return tf.remove_rows_by_column_name(
            CommentLike,
            row_id,
            col_name='CommentId'
        )


def add_comment_like(row_dict):
    return tf.add_row(CommentLike, row_dict)


def update_comment_like(comment_like_row, col_name, new_value):
    return tf.update_row_column(comment_like_row, col_name, new_value)


def search_comment_like(col_name, value):
    return tf.get_rows_like_column_value(CommentLike, col_name, value)


if __name__ == '__main__':
    pass
