from models import Base, Fornecedor, Material
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class MaterialHasFornecedor(Base):
    __tablename__ = "material_has_fornecedor"
    material_id: Mapped[int] = mapped_column("material_id", MEDIUMINT, ForeignKey(Material.id),
                                             nullable=False, primary_key=True)
    fornecedor_id: Mapped[int] = mapped_column("fornecedor_id", MEDIUMINT, ForeignKey(Fornecedor.id),
                                               nullable=False, primary_key=True)
