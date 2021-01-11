from app.Data.db import Base
import sqlalchemy as sa


class Location(Base):
    Id = sa.Column(sa.Integer, autoincrement=True, nullable=False)
    Place = sa.Column(sa.String(45), nullable=False)
    Longitude = sa.Column(sa.DECIMAL(6, 3), nullable=False)
    Latitude = sa.Column(sa.DECIMAL(6, 3), nullable=False)
    Name = sa.Column(sa.String(45))
    UserId = sa.Column(sa.Integer, sa.ForeignKey('user.Id'), nullable=False)
    CategoryId = sa.Column(sa.Integer, sa.ForeignKey('category.Id'), nullable=False)


if __name__ == '__main__':
    location = Location()
