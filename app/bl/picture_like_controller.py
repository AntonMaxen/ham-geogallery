import app.data.repository.picture_like_repo as plr


def get_amount_of_likes_by_picture_id(picture_id):
    picture_likes = plr.get_pic_likes_by_picture_id(picture_id)
    if picture_likes is not None:
        return {
            'likes': len([l for l in picture_likes if l.Liked])
        }


if __name__ == '__main__':
    print(get_amount_of_likes_by_picture_id(3))
