import app.data.repository.user_repo as ur


def get_user_by_email(email):
    user = ur.search_user('Email', email)
    if len(user) > 0:
        return user[0]
    else:
        return None


def get_user_by_id(user_id):
    return ur.get_user_by_id(user_id);


def add_user(row_dict):
    return ur.add_user(row_dict)


def update_user_column(user, col_name, new_value):
    return ur.update_user(user, col_name, new_value)


def update_user_columns(user, update_dict):
    for k, v in update_dict.items():
        update_user_column(user, k, v)


