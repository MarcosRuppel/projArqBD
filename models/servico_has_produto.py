from models import Base, Servico, Produto
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class ServicoHasProduto(Base):
    __tablename__ = "servico_has_produto"
    servico_id: Mapped[int] = mapped_column("servico_id", MEDIUMINT, ForeignKey(Servico.id),
                                            nullable=False, autoincrement=True, primary_key=True)
    produto_id: Mapped[int] = mapped_column("produto_id", MEDIUMINT, ForeignKey(Produto.id),
                                            nullable=False, primary_key=True)
    qtde: Mapped[int] = mapped_column("qtde", MEDIUMINT, nullable=False, default=0)

