from app.Data.db import Base
import sqlalchemy as sa


class UserBadge(Base):
    __tablename__ = 'user_has_badge'

    UserId = sa.Column(sa.Integer, sa.ForeignKey('user.Id'), nullable=False)
    BadgeId = sa.Column(sa.Integer, sa.ForeignKey('badge.Id'), nullable=False)
    DateAcquired = sa.Column(sa.Date, nullable=False)


if __name__ == '__main__':
    user_has_badge = UserBadge()
