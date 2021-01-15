import app.Data.databuilder.genModels.generator as gen
from app.Data.models.model_imports import *
import app.Data.repository.table_functions as tf


class GenLocation:
    def __init__(self):
        location = gen.get_random_location()
        self.Place = location[2]
        self.Longitude = location[1]
        self.Latitude = location[0]
        self.Name = gen.get_random_word()
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, "Id", None)
        random_category = tf.get_random_row(Category)
        self.CategoryId = getattr(random_category, "Id", None)


if __name__ == '__main__':
    loc = GenLocation()
    print(loc.__dict__)
