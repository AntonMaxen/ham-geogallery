from app.Data.db import session
from sqlalchemy.sql.expression import func
from sqlalchemy import exc
import datetime


def get_all_rows(model):
    # Return all rows in given table
    return session.query(model).all()


def get_row_by_column(model, row_id, col_name='Id'):
    # Returns First row that matches model.col_name == row_id
    return session.query(model) \
        .filter(getattr(model, col_name) == row_id) \
        .first()


def get_rows_like_column_value(model, col_name, value):
    """Return all rows that contains model.col_name LIKE value
    Good way to search database. """
    return session.query(model) \
        .filter(getattr(model, col_name)) \
        .ilike(f'%{value}%') \
        .all()


def validate_number(number):
    if isinstance(number, int):
        return True

    if isinstance(number, str) and number.isdigit():
        return True

    return False


def add_row(model, new_row):
    """ Adds row to database table with a new_row dictionary
    Make a dict that matches column names in given table."""
    try:
        row = model(**new_row)
        session.add(row)
        session.commit()
    except exc.SQLAlchemyError:
        print('rollback add_row')
        session.rollback()
        return None

    return row


def update_row_column(model_obj, col_name, new_value):
    # updates a column (col_name) in a given row (model_obj) with (new_value)
    try:
        setattr(model_obj, col_name, new_value)
        session.commit()
    except exc.SQLAlchemyError:
        print('rollback update_row_column')
        session.rollback()
        return None

    return model_obj


def remove_row_by_id(model, row_id, col_name='Id'):
    # Removes row from table (model) that matches (model.col_name) == (row_id)
    try:
        obj = session.query(model) \
            .filter(getattr(model, col_name) == row_id) \
            .one()

        session.delete(obj)
        session.commit()
    except exc.SQLAlchemyError:
        print('rollback remove_row_by_id')
        session.rollback()
        return None

    return obj


def get_columns(model_obj):
    # Returns Names of the columns for a given Table (model_obj).
    return [column.key for column in model_obj.__table__.columns]


def row_to_dict(row):
    return {column: getattr(row, column, None)
            for column in get_columns(row)}


def refresh_row(model_obj):
    """Refreshes the sqla object, used after a commit on given object.
    if no refresh is done on a commited object, the object will have
    unexpected behaviour."""
    session.refresh(model_obj)


def get_random_row(model):
    return session.query(model).order_by(func.random()).first()


if __name__ == '__main__':
    user = {
        "FirstName": "anton",
        "LastName": "maxen",
        "Email": "Goiode@mail.com",
        "Username": "hehehe",
        "Hash": "fsgsdlkjtglksj5432lk",
        "Salt": "4243234",
        "PhoneNumber": "435363463",
        "DateOfBirth": datetime.date.today(),
        "JoinDate": datetime.date.today(),
        "PermissionLevel": 5
    }


