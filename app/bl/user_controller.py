import app.data.repository.user_repo as ur


def get_user_by_email(email):
    user = ur.search_user('Email', email)
    if len(user) > 0:
        return user[0]
    else:
        return None


def add_user_token(user_row):
    return ur.add_user_token(user_row)


def remove_user_token(user_row):
    return ur.remove_user_token(user_row)


def remove_user_by_id(user_id):
    return ur.remove_user_by_id(user_id)


def remove_user_by_username(username):
    return ur.remove_user_by_username(username)


def get_user_by_token(token):
    return ur.get_user_by_token(token)


def get_user_by_id(user_id):
    return ur.get_user_by_id(user_id)


def get_user_by_username(username):
    return ur.get_user_by_username(username)


def add_user(row_dict):
    return ur.add_user(row_dict)


def update_user_column(user, col_name, new_value):
    return ur.update_user(user, col_name, new_value)


def update_user_columns(user, update_dict):
    for k, v in update_dict.items():
        update_user_column(user, k, v)


if __name__ == '__main__':
    pass
