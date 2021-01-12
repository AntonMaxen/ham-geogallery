from sqlalchemy.orm import relationship
from app.Data.db import Base
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
        sa.ForeignKey('category.Id', ondelete='CASCADE'),
        nullable=False,
        default=0)

    location = relationship('Location', back_populates='category')
    category = relationship('Category', back_populates='category')


if __name__ == "__main__":
    category = Category()
