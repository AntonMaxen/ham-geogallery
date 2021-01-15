from app.Data.db import session
from app.Data.models.model_imports import *
from app.Data.databuilder.genModels.category import GenCategory
from app.Data.databuilder.genModels.user import GenUser
from app.Data.databuilder.genModels.location import GenLocation
from app.Data.databuilder.genModels.rating import GenRating
from app.Data.databuilder.genModels.visited_location import GenVisitedLocation
from app.Data.databuilder.genModels.picture import GenPicture
from app.Data.databuilder.genModels.picture_like import GenPictureLike
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


def populate_db():
    add_rows(Category, GenCategory, 10)
    add_rows(User, GenUser, 10)
    add_rows(Location, GenLocation, 10)
    add_rows(Rating, GenRating, 10)
    add_rows(VisitedLocation, GenVisitedLocation, 10)
    add_rows(Picture, GenPicture, 10)
    add_rows(PictureLike, GenPictureLike, 10)


if __name__ == '__main__':
    populate_db()
