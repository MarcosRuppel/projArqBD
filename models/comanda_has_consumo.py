from models import Base, Comanda, Consumo
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class ComandaHasConsumo(Base):
    __tablename__ = "comanda_has_consumo"
    comanda_id: Mapped[int] = mapped_column("comanda_id", MEDIUMINT, ForeignKey(Comanda.id),
                                            nullable=False, autoincrement=True, primary_key=True)
    consumo_id: Mapped[int] = mapped_column("consumo_id", MEDIUMINT, ForeignKey(Consumo.id),
                                            nullable=False, primary_key=True)
