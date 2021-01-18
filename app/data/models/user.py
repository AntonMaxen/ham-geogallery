from app.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    Id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True
    )
    FirstName = sa.Column(
        sa.String(45),
        nullable=False
    )
    LastName = sa.Column(
        sa.String(45),
        nullable=False
    )
    Email = sa.Column(
        sa.String(45),
        nullable=False,
        unique=True
    )
    Username = sa.Column(
        sa.String(45),
        nullable=False,
        unique=True
    )
    Hash = sa.Column(
        sa.String(255),
        nullable=False
    )
    Salt = sa.Column(
        sa.String(255),
        nullable=False
    )
    PhoneNumber = sa.Column(
        sa.String(45),
        nullable=False,
        unique=True
    )
    DateOfBirth = sa.Column(
        sa.Date
    )
    JoinDate = sa.Column(
        sa.Date,
        nullable=False
    )
    PermissionLevel = sa.Column(
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
