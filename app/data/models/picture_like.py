from app.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class PictureLike(Base):
    __tablename__ = 'picture_like'

    PictureId = sa.Column(
        sa.Integer,
        sa.ForeignKey('picture.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False)
    UserId = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False)
    Liked = sa.Column(
        sa.Boolean,
        nullable=False)

    picture = relationship('Picture', back_populates='picture_like')
    user = relationship('User', back_populates='picture_like')


if __name__ == "__main__":
    picture_like = PictureLike()
