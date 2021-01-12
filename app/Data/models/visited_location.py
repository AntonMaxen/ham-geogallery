from app.Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class VisitedLocation(Base):
    __tablename__ = 'visited_location'

    LocationId = sa.Column(
        sa.Integer,
        sa.ForeignKey('location.Id', ondelete='CASCADE'),
        nullable=False)
    UserId = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.Id', ondelete='CASCADE'),
        nullable=False)

    location = relationship('Location', back_populates='visited_location')
    user = relationship('User', back_populates='visited_location')


if __name__ == '__main__':
    visited_location = VisitedLocation()
