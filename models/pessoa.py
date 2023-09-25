from models import Base
from sqlalchemy import DECIMAL, DATE, CHAR, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from datetime import datetime


class Pessoa(Base):
    __tablename__ = "pessoa"
    idpessoa: Mapped[int] = mapped_column("idpessoa", MEDIUMINT, nullable=False, autoincrement=True,
                                          primary_key=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(50), nullable=False)
    telefone: Mapped[float] = mapped_column("telefone", DECIMAL(11), nullable=True)
    endereco: Mapped[str] = mapped_column("endereco", VARCHAR(100), nullable=True)
    data_nasc: Mapped[datetime] = mapped_column("data_nasc", DATE, nullable=True)
    CPF: Mapped[str] = mapped_column("CPF", CHAR(11), nullable=False, unique=True)
