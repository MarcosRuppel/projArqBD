from models import Base
from sqlalchemy import DECIMAL, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class Consumo(Base):
    __tablename__ = "consumo"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, nullable=False, primary_key=True)
    descricao: Mapped[str] = mapped_column("descricao", VARCHAR(45), nullable=False)
    valor_unit: Mapped[float] = mapped_column("valor_unit", DECIMAL(10, 2), nullable=False,
                                              default=0.00)
