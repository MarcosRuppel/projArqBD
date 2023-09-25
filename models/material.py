from models import Base
from sqlalchemy import DECIMAL, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class Material(Base):
    __tablename__ = "material"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(50), nullable=False)
    tipo: Mapped[str] = mapped_column("tipo", VARCHAR(20), nullable=False)
    custo: Mapped[float] = mapped_column("custo", DECIMAL(10, 2), nullable=False,
                                         default="0.00")
    qtd_estoque: Mapped[int] = mapped_column("qtd_estoque", MEDIUMINT, nullable=False, default=0)
