import app.Data.repository.table_functions as tf
from app.Data.models.model_imports import *


def get_all_pic_likes():
    return tf.get_all_rows(PictureLike)


# pic_or_user_id input as a string
def get_pic_like_by_id(row_id, pic_or_user_id):
    if tf.validate_number(row_id):
        return tf.get_row_by_column(PictureLike, row_id, pic_or_user_id)


def add_pic_like(row_dict):
    return tf.add_row(PictureLike, row_dict)


def update_pic_like(category_row, col_name, new_value):
    return tf.update_row_column(category_row, col_name, new_value)


def get_liked_pictures(pic_id):
    tf.get_row_by_column(PictureLike, "Picture_id", pic_id)


def get_user_that_liked_pictures(pic_id):
    tf.get_row_by_column(PictureLike, "User_id", pic_id)


def unlike(row_id):
    tf.remove_row_by_id(PictureLike, row_id)
