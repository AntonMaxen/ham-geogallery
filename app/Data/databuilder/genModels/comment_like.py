from app.Data.models.model_imports import *
import app.Data.databuilder.utils.generator as gen
import app.Data.repository.table_functions as tf


class GenCommentLike:
    def __init__(self):
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, 'Id', None)
        random_comment = tf.get_random_row(Comment)
        self.CommentId = getattr(random_comment, 'Id', None)
        self.Liked = gen.get_random_number(0, 1)


if __name__ == '__main__':
    gen_comment_like = GenCommentLike()
    print(gen_comment_like.__dict__)
