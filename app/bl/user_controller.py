import app.data.repository.user_repo as ur

def get_user_by_email(email):
    user = ur.search_user('Email', email)
    if len(user) > 0:
        return user[0]
    else:
        return None


def add_user(row_dict):
    return ur.add_user(row_dict)
