from sqlalchemy.orm import relationship
from app.data.db import Base
import sqlalchemy as sa


class Category(Base):
    __tablename__ = 'category'

    Id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True)
    Name = sa.Column(
        sa.String(45),
        nullable=False)
    ParentId = sa.Column(
        sa.Integer,
        sa.ForeignKey('category.Id', ondelete='CASCADE'))

    location = relationship('Location', back_populates='category')
