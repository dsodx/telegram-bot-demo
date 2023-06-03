from sqlalchemy import BIGINT, VARCHAR, INTEGER
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    n = mapped_column(INTEGER, primary_key=True)
    id = mapped_column(BIGINT, unique=True, nullable=False)
    name = mapped_column(VARCHAR, nullable=False)
