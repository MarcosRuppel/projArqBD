from models import Base, Comanda
from sqlalchemy import DECIMAL, VARCHAR, BIGINT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class Recebimento(Base):
    __tablename__ = "recebimento"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    NF: Mapped[int] = mapped_column("NF", BIGINT, nullable=False)
    valor_pago: Mapped[float] = mapped_column("valor_pago", DECIMAL(10, 2), nullable=False,
                                              default=0.00)
    forma_pgto: Mapped[str] = mapped_column("forma_pgto", VARCHAR(15), nullable=False, default="A VISTA")
    comanda_id: Mapped[int] = mapped_column("comanda_id", MEDIUMINT, ForeignKey(Comanda.id),
                                            nullable=False)
