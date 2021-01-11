from app.Data.db import Base
import sqlalchemy as sa


class User(Base):
    __tablename__ = 'user'

    Id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    FirstName = sa.Column(sa.String(45), nullable=False)
    LastName = sa.Column(sa.String(45), nullable=False)
    Email = sa.Column(sa.String(45), nullable=False, unique=True)
    Username = sa.Column(sa.String(45), nullable=False, unique=True)
    Hash = sa.Column(sa.String(255), nullable=False)
    Salt = sa.Column(sa.String(45), nullable=False)
    PhoneNumber = sa.Column(sa.String(45), nullable=False, unique=True)
    DateOfBirth = sa.Column(sa.Date, nullable=False)
    JoinDate = sa.Column(sa.Date, nullable=False)
    PermissionLevel = sa.Column(sa.Integer, nullable=False)


if __name__ == '__main__':
    user = User()
