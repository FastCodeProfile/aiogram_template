from datetime import datetime as dt
from enum import IntEnum

from sqlalchemy import BigInteger, Column, Enum, DateTime

from .base import Base


class Role(IntEnum):
    USER = 0
    MODERATOR = 1
    ADMINISTRATOR = 2


class UserModel(Base):
    """
    Основная модель пользователей
    """

    __tablename__ = "users"  # Имя таблицы
    id = Column(
        BigInteger, nullable=False, primary_key=True
    )  # telegram id пользователя
    role = Column(Enum(Role), default=Role.USER)  # Роль пользователя в проекте
    update_date = Column(
        DateTime, default=dt.today(), onupdate=dt.today()
    )  # Дата обновления пользователя
    registration_date = Column(
        DateTime, default=dt.today()
    )  # Дата регистрации пользователя

    def __str__(self) -> str:
        """
        Возвращает ID пользователя

        :param self: User

        :return: str
        """
        return f"User ID: {self.id}"
