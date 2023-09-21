from models import Base, Comanda
from sqlalchemy import DECIMAL, BOOLEAN, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class Cobranca(Base):
    __tablename__ = "cobranca"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, primary_key=True)
    valor: Mapped[float] = mapped_column("valor", DECIMAL(10, 2), nullable=False, default=0.00)
    comanda_id: Mapped[int] = mapped_column("comdanda_id", MEDIUMINT,
                                            ForeignKey(Comanda.id), nullable=False)
    comanda_cliente_id: Mapped[int] = mapped_column("comdanda_cliente_id", MEDIUMINT,
                                                    ForeignKey(Comanda.cliente_id), nullable=False)
    comanda_funcionario_id: Mapped[int] = mapped_column("comdanda_funcionario_id", MEDIUMINT,
                                                        ForeignKey(Comanda.funcionario_id), nullable=False)
    quitada: Mapped[bool] = mapped_column("quitada", BOOLEAN, nullable=False, default=0)
