from app.Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Picture(Base):
    __tablename__ = 'picture'

    Id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False)
    ImageName = sa.Column(
        sa.String(45),
        nullable=False)
    Date = sa.Column(
        sa.Date,
        nullable=False)
    UserId = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.Id', ondelete='CASCADE'),
        nullable=False)
    LocationId = sa.Column(
        sa.Integer,
        sa.ForeignKey('location.Id', ondelete='CASCADE'),
        nullable=False)
    FileName = sa.Column(
        sa.String(45),
        nullable=False,
        unique=True)

    user = relationship('User', back_populates='picture')
    location = relationship('Location', back_populates='picture')
    picture_like = relationship('PictureLike', back_populates='picture')


if __name__ == "__main__":
    picture = Picture()
    print('picture')
