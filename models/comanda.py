from models import Base, Cliente
from sqlalchemy import DATETIME, DECIMAL, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT, SMALLINT
from datetime import datetime


class Comanda(Base):
    __tablename__ = "comanda"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    num_mesa: Mapped[int] = mapped_column("num_mesa", SMALLINT, nullable=True)
    criada_em: Mapped[datetime] = mapped_column("criada_em", DATETIME, nullable=False,
                                                default=func.current_timestamp())
    valor_comanda: Mapped[float] = mapped_column("valor_comanda", DECIMAL(10, 2),
                                                 nullable=True, default="0.00")
    cliente_id: Mapped[int] = mapped_column("cliente_id", MEDIUMINT, ForeignKey(Cliente.id),
                                            nullable=False)
