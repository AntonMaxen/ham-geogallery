from app.data.models.model_imports import *
import app.data.databuilder.utils.generator as gen
import app.data.repository.table_functions as tf


class GenPictureLike:
    def __init__(self):
        random_picture = tf.get_random_row(Picture)
        self.PictureId = getattr(random_picture, 'Id', None)
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, 'Id', None)
        self.Liked = gen.get_random_number(0, 1)
