from app.data.models.model_imports import *
import app.data.databuilder.utils.generator as gen
import app.data.repository.table_functions as tf


class GenComment:
    def __init__(self):
        self.CommentText = gen.get_random_text(
            max_chars=gen.get_random_number(5, 255)
        )
        random_review = tf.get_random_row(Review)
        self.ReviewId = getattr(random_review, 'Id', None)
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, 'Id', None)
