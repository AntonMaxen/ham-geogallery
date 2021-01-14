from app.Data.db import session
from app.Data.models.model_imports import *
from app.Data.databuilder.genModels.category import GenCategory
from sqlalchemy import exc


def add_rows(model, gen_model, amount):
    try:
        for _ in range(amount):
            data_dict = gen_model().__dict__
            session.add(model(**data_dict))
            session.commit()
    except exc.SQLAlchemyError:
        session.rollback()


def add_row(model, gen_model):
    add_rows(model, gen_model, 1)


def populate_db():
    add_rows(Category, GenCategory, 1000)


if __name__ == '__main__':
    populate_db()
