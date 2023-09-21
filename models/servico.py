from models import Base
from sqlalchemy import DECIMAL, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class Servico(Base):
    __tablename__ = "servico"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, primary_key=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(45), nullable=False)
    valor: Mapped[float] = mapped_column("valor", DECIMAL(10, 2), nullable=False, default=0.00)
