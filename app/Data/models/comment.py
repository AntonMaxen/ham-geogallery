from app.Data.db import Base
import sqlalchemy as sa


class Comment(Base):
    __tablename__ = 'comment'

    Id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    CommentText = sa.Column(sa.String(255), nullable=False)
    ReviewId = sa.Column(sa.Integer, sa.ForeignKey('review.Id'), nullable=False)
    UserId = sa.Column(sa.Integer, sa.ForeignKey('user.Id'), nullable=False)


if __name__ == "__main__":
    comment = Comment()
