from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.crud.base import CRUDBase
from src.menu.models import Menu, Submenu


class MenuCrud(CRUDBase):
    async def select_all_data(self, session):
        result = await session.scalars(
            select(self.model).options(
                joinedload(self.model.submenus).joinedload(Submenu.dishes)
            )
        )
        menus = result.unique().all()
        menu_data = jsonable_encoder(menus)
        return menu_data


menu_crud = MenuCrud(Menu)
