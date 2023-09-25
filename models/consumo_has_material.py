from models import Base, Consumo, Material
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT, SMALLINT


class ConsumoHasMaterial(Base):
    __tablename__ = "consumo_has_material"
    consumo_id: Mapped[int] = mapped_column("consumo_id", MEDIUMINT, ForeignKey(Consumo.id),
                                            nullable=False, autoincrement=True, primary_key=True)
    material_id: Mapped[int] = mapped_column("material_id", MEDIUMINT, ForeignKey(Material.id),
                                             nullable=False, primary_key=True)
    qtde_material: Mapped[int] = mapped_column("qtde", SMALLINT, nullable=False, default=0)
