from models import Base, Cliente, Funcionario
from sqlalchemy import DATETIME, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT, SMALLINT
from datetime import datetime


class Comanda(Base):
    __tablename__ = "comanda"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    num_mesa: Mapped[int] = mapped_column("num_mesa", SMALLINT, nullable=False)
    cliente_id: Mapped[int] = mapped_column("cliente_id", MEDIUMINT, ForeignKey(Cliente.id),
                                            nullable=False)
    criado_em: Mapped[datetime] = mapped_column("data_contratacao", DATETIME, nullable=False,
                                                default=func.current_date())
    funcionario_id: Mapped[int] = mapped_column("funcionario_id", MEDIUMINT, ForeignKey(Funcionario.id),
                                                nullable=False)
