from app.data.models.model_imports import *
import app.data.databuilder.utils.generator as gen
import app.data.repository.table_functions as tf


class GenReviewLike:
    def __init__(self):
        random_review = tf.get_random_row(Review)
        self.ReviewId = getattr(random_review, 'Id', None)
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, 'Id', None)
        self.Liked = gen.get_random_number(0, 1)
