from models import Base
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class Estoque(Base):
    __tablename__ = "estoque"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(50), nullable=False)
    qtde: Mapped[int] = mapped_column("qtde", MEDIUMINT, nullable=False, default=0)
    qte_min: Mapped[int] = mapped_column("qtde_min", MEDIUMINT, nullable=False, default=0)
