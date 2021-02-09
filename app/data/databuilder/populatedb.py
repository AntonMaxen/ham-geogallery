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
from app.utils import print_dict
# external imports
from sqlalchemy import exc


def add_rows(model, gen_model, amount):
    rows = []
    for i in range(amount):
        try:
            progress = int((i / amount) * 100)
            print('['+'-' * progress + '>' + ' ' * (100 - (progress+1)) + ']')
            data_dict = gen_model().__dict__
            print_dict(data_dict)
            row = model(**data_dict)
            session.add(row)
            session.commit()
            rows.append(row)
        except exc.SQLAlchemyError as e:
            print(e)
            session.rollback()

    return rows


def add_row(model, gen_model):
    rows = add_rows(model, gen_model, 1)
    return rows[0] if len(rows) > 0 else None


def populate_db(amount=100):
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


def add_categories(amount=100):
    return add_rows(Category, GenCategory, amount)


def add_users(amount=100):
    return add_rows(User, GenUser, amount)


def add_locations(amount=100):
    return add_rows(Location, GenLocation, amount)


def add_ratings(amount=100):
    return add_rows(Rating, GenRating, amount)


def add_visited_locations(amount=100):
    return add_rows(VisitedLocation, GenVisitedLocation, amount)


def add_pictures(amount=100):
    return add_rows(Picture, GenPicture, amount)


def add_picture_likes(amount=100):
    return add_rows(PictureLike, GenPictureLike, amount)


def add_reviews(amount=100):
    return add_rows(Review, GenReview, amount)


def add_review_likes(amount=100):
    return add_rows(ReviewLike, GenReviewLike, amount)


def add_comments(amount=100):
    return add_rows(Comment, GenComment, amount)


def add_comment_likes(amount=100):
    return add_rows(CommentLike, GenCommentLike, amount)


def add_badges(amount=100):
    return add_rows(Badge, GenBadge, amount)


def add_user_badges(amount=100):
    return add_rows(UserBadge, GenUserBadge, amount)


if __name__ == '__main__':
    populate_db(amount=10)
