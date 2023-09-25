from models import Base, Pessoa
from sqlalchemy import DATETIME, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from datetime import datetime


class Cliente(Base):
    __tablename__ = "cliente"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    desde: Mapped[datetime] = mapped_column("desde", DATETIME, nullable=False,
                                            default=func.current_timestamp())
    pessoa_idpessoa: Mapped[int] = mapped_column("pessoa_idpessoa", MEDIUMINT,
                                                 ForeignKey(Pessoa.idpessoa), nullable=False, primary_key=True)
