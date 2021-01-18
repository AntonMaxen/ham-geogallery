from sqlalchemy.orm import relationship

from app.data.db import Base
import sqlalchemy as sa


class UserBadge(Base):
    __tablename__ = 'user_has_badge'

    UserId = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False)
    BadgeId = sa.Column(
        sa.Integer,
        sa.ForeignKey('badge.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False)
    DateAcquired = sa.Column(
        sa.Date,
        nullable=False)

    badge = relationship('Badge', back_populates='user_has_badge')
    user = relationship('User', back_populates='user_has_badge')


if __name__ == '__main__':
    user_has_badge = UserBadge()
    print(user_has_badge)
