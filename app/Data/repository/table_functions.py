from app.Data.db import session
from app.Data.models.model_imports import *
import datetime


def get_all_rows(model):
    return session.query(model).all()


def get_row_by_column(model, row_id, col_name='Id'):
    return session.query(model) \
        .filter(getattr(model, col_name) == row_id).first()


# User
def add_row(model, new_row):
    try:
        row = model(**new_row)
        session.add(row)
        session.commit()
    except:
        print('rollback')
        session.rollback()


# user obj
def update_row_column(model_obj, column_name, new_value):
    try:
        setattr(model_obj, column_name, new_value)
        session.commit()
    except:
        print('rollback')
        session.rollback()


def remove_row_by_id(model, row_id, col_name='Id'):
    try:
        session.query(model) \
            .filter(getattr(model, col_name) == row_id).delete()
        session.commit()
    except:
        print('rollback')
        session.rollback()


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

    current_row = get_row_by_column(User, 2)
    current_row.FirstName = "Anton"
    print(current_row.FirstName)

    update_row_column(current_row, "FirstName", "Inte anton")
    print(current_row.FirstName)



