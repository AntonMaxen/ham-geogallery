import app.data.repository.review_like_repo as rlr


def get_amount_of_likes_by_review_id(review_id):
    review_likes = rlr.get_review_likes_by_review_id(review_id)
    if review_likes is not None:
        return {
            'likes': len([l for l in review_likes if l.Liked])
        }


if __name__ == '__main__':
    print(get_amount_of_likes_by_review_id(7))
