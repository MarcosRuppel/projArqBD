from models import Base
from sqlalchemy import DECIMAL, DATE, CHAR, VARCHAR, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from datetime import datetime


class Funcionario(Base):
    __tablename__ = "funcionario"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(50), nullable=False)
    funcao: Mapped[str] = mapped_column("funcao", VARCHAR(50), nullable=False)
    salario: Mapped[float] = mapped_column("salario", DECIMAL(10, 2), nullable=False,
                                           default="0.00")
    CPF: Mapped[str] = mapped_column("CPF", CHAR(11), nullable=False, unique=True)
    telefone: Mapped[int] = mapped_column("telefone", DECIMAL(11), nullable=True)
    data_nasc: Mapped[datetime] = mapped_column("data_nasc", DATE, nullable=True)
    data_contratacao: Mapped[datetime] = mapped_column("data_contratacao", DATE, nullable=False,
                                                       default=func.current_date())
