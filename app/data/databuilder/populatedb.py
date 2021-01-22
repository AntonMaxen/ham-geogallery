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
    try:
        for _ in range(amount):
            data_dict = gen_model().__dict__
            print(data_dict)
            session.add(model(**data_dict))
            session.commit()
    except exc.SQLAlchemyError:
        session.rollback()


def add_row(model, gen_model):
    add_rows(model, gen_model, 1)


def populate_db(amount=10):
    add_rows(Category, GenCategory, amount)
    add_rows(User, GenUser, amount)
    add_rows(Location, GenLocation, amount)
    add_rows(Rating, GenRating, amount)
    add_rows(VisitedLocation, GenVisitedLocation, amount)
    add_rows(Picture, GenPicture, amount)
    add_rows(PictureLike, GenPictureLike, amount)
    add_rows(Review, GenReview, amount)
    add_rows(ReviewLike, GenReviewLike, amount)
    add_rows(Comment, GenComment, amount)
    add_rows(CommentLike, GenCommentLike, amount)
    add_rows(Badge, GenBadge, amount)
    add_rows(UserBadge, GenUserBadge, amount)


def populate_pictures(amount=1000):
    add_rows(Picture, GenPicture, amount)


if __name__ == '__main__':
    populate_db()
