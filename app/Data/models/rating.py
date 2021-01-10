from app.Data.db import Base
import sqlalchemy as sa


class Rating(Base):
    __tablename__ = 'rating'

    UserId = sa.Column(sa.Integer, sa.ForeignKey('user.Id'), nullable=False)
    LocationId = sa.Column(sa.Integer, sa.ForeignKey('location.Id'), nullable=False)
    Score = sa.Column(sa.Numeric(2, 1), nullable=False)

if __name__ == "__main__":
    rating = Rating()
