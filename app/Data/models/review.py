from sqlalchemy.orm import relationship
from app.Data.db import Base
import sqlalchemy as sa


class Review(Base):
    __tablename__ = 'review'

    Id = sa.Column(
        sa.Integer,
        nullable=False,
        autoincrement=True)
    Title = sa.Column(
        sa.String(45),
        nullable=False)
    ReviewText = sa.Column(
        sa.String(1024),
        nullable=False)
    Score = sa.Column(
        sa.DECIMAL(2, 1),
        nullable=False)
    DateCreated = sa.Column(
        sa.Date,
        nullable=False)
    UserId = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.Id', ondelete='Cascade'),
        nullable=False)
    LocationId = sa.Column(
        sa.Integer,
        sa.ForeignKey('location.Id', ondelete='Cascade'),
        nullable=False)

    user = relationship('User', back_populates='review')
    location = relationship('Location', back_populates='review')
    comment = relationship('Comment', back_populates='review')
    review_like = relationship('ReviewLike', back_populates='review')

if __name__ == "__main__":
    review = Review()
