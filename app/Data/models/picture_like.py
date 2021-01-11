from app.Data.db import Base
import sqlalchemy as sa


class PictureLike(Base):
    __tablename__ = 'picture_like'

    PictureId = sa.Column(sa.Integer, primary_key=True, nullable=False)
    UserId = sa.Column(sa.Integer, primary_key=True, nullable=False)
    Liked = sa.Column(sa.Boolean, nullable=False)


if __name__ == "__main__":
    picture_like = PictureLike()
