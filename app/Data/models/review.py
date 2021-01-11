from app.Data.db import Base
import sqlalchemy as sa


class Review(Base):
    __tablename__ = 'review'

    Id = sa.Column(sa.Integer, nullable=False, autoincrement=True)
    Title = sa.Column(sa.String(45), nullable=False)
    ReviewText = sa.Column(sa.String(1024), nullable=False)
    Score = sa.Column(sa.DECIMAL(2, 1), nullable=False)
    DateCreated = sa.Column(sa.Date, nullable=False)
    UserId = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.Id'),
        nullable=False)
    LocationId = sa.Column(
        sa.Integer,
        sa.ForeignKey('location.Id'),
        nullable=False)

if __name__ == "__main__":
    review = Review()
