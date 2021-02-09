from app.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Location(Base):
    __tablename__ = 'location'

    Id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False)
    Place = sa.Column(
        sa.String(45),
        nullable=False)
    Longitude = sa.Column(
        sa.DECIMAL(18, 15),
        nullable=False)
    Latitude = sa.Column(
        sa.DECIMAL(17, 15),
        nullable=False)
    Name = sa.Column(
        sa.String(45),
        nullable=False)
    UserId = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.Id', ondelete='SET NULL'))
    CategoryId = sa.Column(
        sa.Integer,
        sa.ForeignKey('category.Id', ondelete='SET NULL'))

    category = relationship('Category', back_populates='location')
    user = relationship('User', back_populates='location')
    picture = relationship(
        'Picture',
        back_populates='location',
        passive_deletes=True
    )
    visited_location = relationship(
        'VisitedLocation',
        back_populates='location',
        passive_deletes=True
    )
    rating = relationship(
        'Rating',
        back_populates='location',
        passive_deletes=True
    )
    review = relationship(
        'Review',
        back_populates='location',
        passive_deletes=True
    )
