from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import submenu_validator
from app.core.db import get_async_session
from app.crud.submenu import submenu_crud
from app.schemas.status import StatusMessage


class SubMenuCache:
    def __init__(self, session):
        self.session = session

    async def get_submenu_list(self, menu_id):
        submenu_list = await submenu_crud.read_all_subobjects(menu_id, self.session)
        return submenu_list

    async def get_submenu(self, submenu_id):
        await submenu_validator.check_exists(submenu_id, self.session)
        submenu = await submenu_crud.get_one(submenu_id, self.session)
        return submenu

    async def create_submenu(self, menu_id, submenu):
        await submenu_validator.check_title(submenu.title, self.session)
        submenu = await submenu_crud.create_subobject(
            menu_id,
            submenu,
            self.session,
        )
        return submenu

    async def update_submenu(self, submenu_id, obj_in):
        submenu = await submenu_validator.check_exists(submenu_id, self.session)
        submenu = await submenu_crud.update(submenu, obj_in, self.session)
        return submenu

    async def delete_submenu(self, submenu_id):
        submenu = await submenu_validator.check_exists(submenu_id, self.session)
        await submenu_crud.delete(submenu, self.session)
        return StatusMessage(
            status=True,
            message="The submenu has been deleted",
        )


async def submenu_service(session: AsyncSession = Depends(get_async_session)):
    return SubMenuCache(session=session)
