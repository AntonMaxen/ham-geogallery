from app.data.db import session
# Model imports
from app.data.models.model_imports import *
# Generator imports
from app.data.databuilder.genModels.category import GenCategory
from app.data.databuilder.genModels.user import GenUser
from app.data.databuilder.genModels.location import GenLocation
from app.data.databuilder.genModels.rating import GenRating
from app.data.databuilder.genModels.visited_location import GenVisitedLocation
from app.data.databuilder.genModels.picture import GenPicture
from app.data.databuilder.genModels.picture_like import GenPictureLike
from app.data.databuilder.genModels.review import GenReview
from app.data.databuilder.genModels.review_like import GenReviewLike
from app.data.databuilder.genModels.comment import GenComment
from app.data.databuilder.genModels.comment_like import GenCommentLike
from app.data.databuilder.genModels.badge import GenBadge
from app.data.databuilder.genModels.user_has_badge import GenUserBadge
# external imports
from sqlalchemy import exc


def add_rows(model, gen_model, amount):
    for i in range(amount):
        try:
            progress = int((i / amount) * 100)
            print('['+'-' * progress + '>' + ' ' * (100 - (progress+1)) + ']')
            data_dict = gen_model().__dict__
            print(data_dict)
            session.add(model(**data_dict))
            session.commit()
        except exc.SQLAlchemyError:
            print('rollback')
            session.rollback()


def add_row(model, gen_model):
    add_rows(model, gen_model, 1)


def populate_db(amount=100):

    add_rows(ReviewLike, GenReviewLike, 1000)
    add_rows(Comment, GenComment, 1000)
    add_rows(CommentLike, GenCommentLike, 1000)
    add_rows(Badge, GenBadge, 100)
    add_rows(UserBadge, GenUserBadge, 1000)


def populate_pictures(amount=100):
    add_rows(Picture, GenPicture, amount)


def populate_reviews(amount=100):
    add_rows(Review, GenReview, amount)


def populate_picture_likes(amount=100):
    add_rows(PictureLike, GenPictureLike, amount)


def populate_users(amount=100):
    add_rows(User, GenUser, amount)


def populate_review_likes(amount=100):
    add_rows(ReviewLike, GenReviewLike, amount)


if __name__ == '__main__':
    populate_db()

