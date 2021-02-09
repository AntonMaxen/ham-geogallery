from sqlalchemy.orm import relationship
from app.data.db import Base
import sqlalchemy as sa


class Review(Base):
    __tablename__ = 'review'

    Id = sa.Column(
        sa.Integer,
        primary_key=True,
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
        sa.ForeignKey('user.Id', ondelete='CASCADE'),
        nullable=False)
    LocationId = sa.Column(
        sa.Integer,
        sa.ForeignKey('location.Id', ondelete='CASCADE'),
        nullable=False)

    user = relationship('User', back_populates='review')
    location = relationship('Location', back_populates='review')
    comment = relationship(
        'Comment',
        back_populates='review',
        passive_deletes=True
    )
    review_like = relationship(
        'ReviewLike',
        back_populates='review',
        passive_deletes=True
    )
