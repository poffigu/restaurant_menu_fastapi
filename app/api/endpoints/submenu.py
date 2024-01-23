from http import HTTPStatus

from fastapi import APIRouter, Depends

from app.cache.services.submenu_service import SubmenuCache, submenu_service
from app.schemas.status import StatusMessage
from app.schemas.submenu import SubmenuCreate, SubmenuOut, SubmenuUpdate

router = APIRouter(
    prefix="/menus/{menu_id}/submenus",
    tags=["Submenus"],
)


@router.get(
    "/",
    response_model=list[SubmenuOut],
    status_code=HTTPStatus.OK,
    summary="Просмотр списка подменю",
)
async def get_all_submenus(
    menu_id: str, service: SubmenuCache = Depends(submenu_service)
) -> list[SubmenuOut]:
    """
    Получение списка всех подменю для конкретного меню
    """
    return await service.get_submenu_list(menu_id)


@router.get(
    "/{submenu_id}",
    response_model=SubmenuOut,
    status_code=HTTPStatus.OK,
    summary="Просмотр конкретного подменю по id",
)
async def get_one_submenu(
    submenu_id: str, service: SubmenuCache = Depends(submenu_service)
) -> SubmenuOut:
    return await service.get_submenu(submenu_id)


@router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    response_model=SubmenuOut,
    summary="Создание подменю",
)
async def create_new_submenu(
    menu_id: str,
    submenu: SubmenuCreate,
    service: SubmenuCache = Depends(submenu_service),
) -> SubmenuOut:
    """
    Создание подменю:

    - **title**: название (должно быть уникальным)
    - **description**: описание (опционально)
    """
    return await service.create_submenu(menu_id, submenu)


@router.patch(
    "/{submenu_id}",
    response_model=SubmenuOut,
    status_code=HTTPStatus.OK,
    summary="Обновление подменю",
)
async def to_update_submenu(
    submenu_id: str,
    obj_in: SubmenuUpdate,
    service: SubmenuCache = Depends(submenu_service),
) -> SubmenuOut:
    """
    Обновление подменю:

    - **title**: обновленное название (должно быть уникальным)
    - **description**: обновленное описание (опционально)
    """
    return await service.update_submenu(submenu_id, obj_in)


@router.delete(
    "/{submenu_id}",
    response_model=StatusMessage,
    status_code=HTTPStatus.OK,
    summary="Удаление подменю по id",
)
async def to_delete_submenu(
    submenu_id: str, service: SubmenuCache = Depends(submenu_service)
) -> StatusMessage:
    return await service.delete_submenu(submenu_id)
