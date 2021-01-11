from app.Data.db import Base
import sqlalchemy as sa


class VisitedLocation(Base):
    __tablename__ = 'visited_location'

    LocationId = sa.Column(sa.Integer, sa.ForeignKey('location.Id'), nullable=False)
    UserId = sa.Column(sa.Integer, sa.ForeignKey('user.Id'), nullable=False)


if __name__ == '__main__':
    visited_location = VisitedLocation()
