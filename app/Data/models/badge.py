from app.Data.db import Base
import sqlalchemy as sa


class Badge(Base):
    __tablename__ = 'badge'

    Id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    Image = sa.Column(sa.BLOB, nullable=False)
    Name = sa.Column(sa.String(45), nullable=False)
    Description = sa.Column(sa.String(255))


if __name__ == "__main__":
    badge = Badge()