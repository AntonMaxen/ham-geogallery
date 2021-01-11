from app.Data.db import Base
import sqlalchemy as sa


class Picture(Base):
    __tablename__ = 'picture'

    Id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False)
    ImageName = sa.Column(sa.String(45), nullable=False)
    Date = sa.Column(sa.Date, nullable=False)
    UserId = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.Id'),
        nullable=False)
    LocationId = sa.Column(
        sa.Integer,
        sa.ForeignKey('location.Id'),
        nullable=False)
    FileName = sa.Column(sa.String(45), nullable=False, unique=True)


if __name__ == "__main__":
    picture = Picture()
