from models import Base
from sqlalchemy import DECIMAL, CHAR, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class Fornecedor(Base):
    __tablename__ = "fornecedor"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(50), nullable=False)
    CNPJ: Mapped[str] = mapped_column("CNPJ", CHAR(14), nullable=False, unique=True)
    telefone: Mapped[int] = mapped_column("telefone", DECIMAL(11), nullable=True)
    endereco: Mapped[str] = mapped_column("endereco", VARCHAR(50), nullable=True)
