from models import Base
from sqlalchemy import DECIMAL, DATE, DATETIME, CHAR, VARCHAR, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from datetime import datetime


class Cliente(Base):
    __tablename__ = "cliente"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(50), nullable=False)
    telefone: Mapped[float] = mapped_column("telefone", DECIMAL(11), nullable=True)
    CPF: Mapped[str] = mapped_column("CPF", CHAR(11), nullable=False, unique=True)
    data_nasc: Mapped[datetime] = mapped_column("data_nasc", DATE, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=func.current_timestamp())
