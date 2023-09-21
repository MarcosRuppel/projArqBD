from models import Base, Fornecedor, Estoque
from sqlalchemy import DECIMAL, VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class Produto(Base):
    __tablename__ = "produto"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(50), nullable=False)
    tipo: Mapped[str] = mapped_column("tipo", VARCHAR(20), nullable=False)
    custo: Mapped[float] = mapped_column("custo", DECIMAL(10, 2), nullable=False,
                                         default="0.00")
    fornecedor_id: Mapped[int] = mapped_column("fornecedor_id", MEDIUMINT, ForeignKey(Fornecedor.id),
                                               nullable=False)
    estoque_id: Mapped[int] = mapped_column("estoque_id", MEDIUMINT, ForeignKey(Estoque.id),
                                            nullable=False)
