from models import Base, Funcionario, Fornecedor
from sqlalchemy import DECIMAL, VARCHAR, DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from datetime import datetime


class Pagamento(Base):
    __tablename__ = "pagamento"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    descricao: Mapped[str] = mapped_column("descricao", VARCHAR(45), nullable=False)
    valor: Mapped[float] = mapped_column("valor", DECIMAL(10, 2), nullable=False,
                                         default=0.00)
    funcionario_id: Mapped[int] = mapped_column("funcionario_id", MEDIUMINT, ForeignKey(Funcionario.id),
                                                nullable=False)
    fornecedor_id: Mapped[int] = mapped_column("fornecedor_id", MEDIUMINT, ForeignKey(Fornecedor.id),
                                               nullable=False)
    data_pagamento: Mapped[datetime] = mapped_column("data_pagamento", DATETIME, nullable=True,
                                                     default="NULL")
