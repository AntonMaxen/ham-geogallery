from app.Data.models.model_imports import *
import app.Data.databuilder.genModels.generator as gen
import app.Data.repository.table_functions as tf


class GenPicture:
    def __init__(self):
        self.ImageName = gen.get_random_word()
        self.Date = gen.get_random_date()
        most_recent_row = tf.get_highest_row(Picture)
        recent_row_id = getattr(most_recent_row, 'Id', 0)
        self.FileName = f'{self.ImageName}{recent_row_id + 1}.PNG'
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, 'Id', None)
        random_location = tf.get_random_row(Location)
        self.LocationId = getattr(random_location, 'Id', None)


if __name__ == '__main__':
    gen_picture = GenPicture()
    print(gen_picture.__dict__)
