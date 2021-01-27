from app.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True
    )
    first_name = sa.Column(
        sa.String(45)
    )
    last_name = sa.Column(
        sa.String(45)
    )
    email = sa.Column(
        sa.String(45),
        nullable=False,
        unique=True
    )
    username = sa.Column(
        sa.String(45),
        nullable=False,
        unique=True
    )
    hashed_password = sa.Column(
        sa.String(255),
        nullable=False
    )
    phone_number = sa.Column(
        sa.String(45),
        unique=True
    )
    date_of_birth = sa.Column(
        sa.Date
    )
    date_created = sa.Column(
        sa.Date,
        nullable=False
    )
    permission_level = sa.Column(
        sa.Integer,
        nullable=False
    )

    review = relationship(
        'Review',
        back_populates='user',
        passive_deletes=True
    )
    review_like = relationship(
        'ReviewLike',
        back_populates='user',
        passive_deletes=True
    )
    comment = relationship(
        'Comment',
        back_populates='user',
        passive_deletes=True
    )
    comment_like = relationship(
        'CommentLike',
        back_populates='user',
        passive_deletes=True
    )
    visited_location = relationship(
        'VisitedLocation',
        back_populates='user',
        passive_deletes=True
    )
    rating = relationship(
        'Rating',
        back_populates='user',
        passive_deletes=True
    )
    picture_like = relationship(
        'PictureLike',
        back_populates='user',
        passive_deletes=True
    )
    picture = relationship(
        'Picture',
        back_populates='user',
        passive_deletes=True
    )
    user_has_badge = relationship(
        'UserBadge',
        back_populates='user',
        passive_deletes=True
    )
    location = relationship(
        'Location',
        back_populates='user'
    )


if __name__ == '__main__':
    user = User()
