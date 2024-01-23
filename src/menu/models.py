import uuid
from sqlalchemy import and_, Column, ForeignKey, func, select, String
from sqlalchemy.orm import declarative_base, declared_attr, column_property, Mapped, relationship


def generate_uuid():
    return str(uuid.uuid4())

class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

Models = declarative_base(cls=PreBase)

class Dish(Models):
    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(String, nullable=False)
    parent_id = Column(String, ForeignKey('submenu.id'))

class Submenu(Models):
    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    parent_id = Column(String, ForeignKey('menu.id'))
    dishes = relationship('Dish', cascade='delete', backref='submenu', lazy='selectin')
    dishes_count: Mapped[int] = column_property(select(func.count(Dish.id)).where(Dish.parent_id == id).scalar_subquery())

class Menu(Models):
    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    submenus = relationship('Submenu', cascade='delete', backref='menu', lazy='selectin')
    submenus_count = column_property(select(func.count(Submenu.id)).where(Submenu.parent_id == id).scalar_subquery())
    dishes_count: Mapped[int] = column_property(select(func.count(Dish.id)).join(Submenu).where(and_(Submenu.parent_id == id, Submenu.id == Dish.parent_id)).correlate_except(Dish).scalar_subquery())
