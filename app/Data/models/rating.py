from app.Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Rating(Base):
    __tablename__ = 'rating'

    UserId = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.Id', ondelete='CASCADE'),
        nullable=False)
    LocationId = sa.Column(
        sa.Integer,
        sa.ForeignKey('location.Id', ondelete='CASCADE'),
        nullable=False)
    Score = sa.Column(
        sa.DECIMAL(2, 1),
        nullable=False)

    location = relationship('Location', back_populates='rating')
    user = relationship('User', back_populates='rating')


if __name__ == "__main__":
    rating = Rating()
