from models import Base, Comanda, Servico
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT, SMALLINT


class ComandaHasServico(Base):
    __tablename__ = "comanda_has_servico"
    comanda_id: Mapped[int] = mapped_column("comanda_id", MEDIUMINT, ForeignKey(Comanda.id),
                                            nullable=False, autoincrement=True, primary_key=True)
    comanda_cliente_id: Mapped[int] = mapped_column("comanda_cliente_id", MEDIUMINT,
                                                    ForeignKey(Comanda.cliente_id), nullable=False,
                                                    primary_key=True)
    comanda_funcionario_id: Mapped[int] = mapped_column("comanda_funcionario_id", MEDIUMINT,
                                                        ForeignKey(Comanda.funcionario_id), nullable=False,
                                                        primary_key=True)
    servico_id: Mapped[int] = mapped_column("servico_id", MEDIUMINT, ForeignKey(Servico.id),
                                            nullable=False, primary_key=True)
    qtde: Mapped[int] = mapped_column("qtde", SMALLINT, nullable=False, default=0)
