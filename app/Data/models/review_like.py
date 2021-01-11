from app.Data.db import Base
import sqlalchemy as sa


class ReviewLike(Base):
    __tablename__ = 'review_like'

    ReviewId = sa.Column(sa.Integer, sa.ForeignKey('review.Id'), nullable=False)
    UserId = sa.Column(sa.Integer, sa.ForeignKey('user.Id'), nullable=False)
    Liked = sa.Column(sa.Boolean, nullable=False)


if __name__ == "__main__":
    review_like = ReviewLike()
