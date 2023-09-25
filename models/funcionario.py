from models import Base, Pessoa
from sqlalchemy import DECIMAL, DATE, VARCHAR, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from datetime import datetime


class Funcionario(Base):
    __tablename__ = "funcionario"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    matricula: Mapped[int] = mapped_column("matricula", MEDIUMINT, nullable=False, autoincrement=True)
    data_contratacao: Mapped[datetime] = mapped_column("data_contratacao", DATE, nullable=False,
                                                       default=func.current_date())
    funcao: Mapped[str] = mapped_column("funcao", VARCHAR(50), nullable=False)
    salario: Mapped[float] = mapped_column("salario", DECIMAL(10, 2), nullable=False,
                                           default="0.00")
    pessoa_idpessoa: Mapped[int] = mapped_column("pessoa_idpessoa", MEDIUMINT,
                                                 ForeignKey(Pessoa.idpessoa), nullable=False, primary_key=True)
