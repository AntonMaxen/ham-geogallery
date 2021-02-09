from werkzeug.security import generate_password_hash
import app.bl.user_controller as uc
import app.bl.location_controller as lc
import app.data.databuilder.populatedb as pdb
import datetime


def create_test_user():
    password = 'test'
    hash_salt = generate_password_hash(
        password,
        method='sha256',
        salt_length=32
    )

    test_user = uc.add_user({
        'FirstName': 'test-firstname',
        'LastName': 'test-lastname',
        'Email': 'test-email@email.com',
        'Username': 'test-username',
        'Hash': hash_salt,
        'PhoneNumber': 'test-phonenumber',
        'DateOfBirth': datetime.date.fromisoformat('1996-05-29'),
        'JoinDate': datetime.date.fromisoformat('2000-01-01'),
        'PermissionLevel': 1
    })

    return test_user, password


def create_test_location(user):
    test_location = lc.add_location({
        'Place': 'test-place',
        'Longitude': 0,
        'Latitude': 0,
        'Name': 'test-name',
        'UserId': user.Id
    })
    return test_location


def remove_test_user():
    return uc.remove_user_by_username('test-username')


def remove_test_locations():
    return lc.remove_locations_by_place_name('test-place')


def create_test_data():
    test_category = pdb.add_categories(amount=1)[0]
    test_user, password = create_test_user()
    test_location = pdb.add_locations(amount=1)[0]
    test_rating = pdb.add_locations(amount=1)[0]
    test_visited_location = pdb.add_visited_locations(amount=1)[0]
    test_picture = pdb.add_pictures(amount=1)[0]
    test_picture_like = pdb.add_picture_likes(amount=1)[0]
    test_review = pdb.add_reviews(amount=1)[0]
    test_review_like = pdb.add_review_likes(amount=1)[0]
    test_comment = pdb.add_comments(amount=1)[0]
    test_comment_like = pdb.add_comment_likes(amount=1)[0]
    test_badge = pdb.add_badges(amount=1)[0]
    test_user_badge = pdb.add_user_badges(amount=1)[0]

    return {
        'category': {'data': test_category},
        'user': {'data': test_user, 'password': password},
        'location': {'data': test_location},
        'rating': {'data': test_rating},
        'visited_location': {'data': test_visited_location},
        'picture': {'data': test_picture},
        'picture_like': {'data': test_picture_like},
        'review': {'data': test_review},
        'review_like': {'data': test_review_like},
        'comment': {'data': test_comment},
        'comment_like': {'data': test_comment_like},
        'badge': {'data': test_badge},
        'user_badge': {'data': test_user_badge}
    }
