from sqlalchemy import BIGINT, VARCHAR, INTEGER
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    n: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    id: Mapped[int] = mapped_column(BIGINT, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR, nullable=False)


class UserProfile(Base):
    __tablename__ = "users_profiles"

    n: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    id: Mapped[int] = mapped_column(BIGINT, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR, nullable=False)
    last_name: Mapped[str] = mapped_column(VARCHAR, nullable=False)
    age: Mapped[str] = mapped_column(INTEGER, nullable=False)
