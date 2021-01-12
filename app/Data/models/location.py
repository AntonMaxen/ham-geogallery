from app.Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Location(Base):
    Id = sa.Column(
        sa.Integer,
        autoincrement=True,
        nullable=False)
    Place = sa.Column(
        sa.String(45), nullable=False)
    Longitude = sa.Column(
        sa.DECIMAL(6, 3),
        nullable=False)
    Latitude = sa.Column(
        sa.DECIMAL(6, 3),
        nullable=False)
    Name = sa.Column(
        sa.String(45))
    UserId = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.Id',
                      ondelete='SET NULL'),
        nullable=True)
    CategoryId = sa.Column(
        sa.Integer,
        sa.ForeignKey('category.Id',
                      ondelete='SET NULL'),
        nullable=True)

    category = relationship('Category', back_populates='location')
    user = relationship('User', back_populates='location')
    picture = relationship('Picture', back_populates='location')
    visited_location = relationship(
        'VisitedLocation', back_populates='location')
    rating = relationship('Rating', back_populates='location')


if __name__ == '__main__':
    location = Location()
