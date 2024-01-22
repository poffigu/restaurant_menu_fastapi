from fastapi import APIRouter, Depends
from app.cache.services.dish_service import DishCache, dish_service
from app.cache.services.menu_service import MenuCache, menu_service
from app.cache.services.submenu_service import SubMenuCache, submenu_service
from app.schemas.dish import DishCreate, DishOut, DishUpdate
from app.schemas.menu import MenuCreate, MenuOut, MenuUpdate
from app.schemas.submenu import SubMenuCreate, SubMenuOut, SubMenuUpdate
from app.schemas.status import StatusMessage


router = APIRouter(prefix='/api/v1/menus')

# CRUD menu
@router.get('', response_model=list[MenuOut], status_code=200, tags=['Menu'])
async def get_all_menus(service: MenuCache = Depends(menu_service)) -> list[MenuOut]:
    return await service.get_menu_list()

@router.get('/{menu_id}', response_model=MenuOut, status_code=200, tags=['Menu'])
async def get_one_menu(menu_id: str, service: MenuCache = Depends(menu_service)) -> MenuOut:
    return await service.get_menu(menu_id)

@router.post('', response_model=MenuOut, status_code=201, tags=['Menu'])
async def create_new_menu(menu: MenuCreate, service: MenuCache = Depends(menu_service)) -> MenuOut:
    return await service.create_menu(menu)

@router.patch('/{menu_id}', response_model=MenuOut, status_code=200, tags=['Menu'])
async def to_update_menu(menu_id: str, obj_in: MenuUpdate, service: MenuCache = Depends(menu_service)) -> MenuOut:
    return await service.update_menu(menu_id, obj_in)

@router.delete('/{menu_id}', response_model=StatusMessage, status_code=200, tags=['Menu'])
async def to_delete_menu(menu_id: str, service: MenuCache = Depends(menu_service)) -> StatusMessage:
    return await service.delete_menu(menu_id)

# CRUD submenu
@router.get('/{menu_id}/submenus', response_model=list[SubMenuOut], status_code=200, tags=['Submenu'])
async def get_all_submenus(menu_id: str, service: SubMenuCache = Depends(submenu_service)) -> list[SubMenuOut]:
    return await service.get_submenu_list(menu_id)

@router.get('/{menu_id}/submenus/{submenu_id}', response_model=SubMenuOut, status_code=200, tags=['Submenu'])
async def get_one_submenu(submenu_id: str, service: SubMenuCache = Depends(submenu_service)) -> SubMenuOut:
    return await service.get_submenu(submenu_id)

@router.post('/{menu_id}/submenus', response_model=SubMenuOut, status_code=201, tags=['Submenu'])
async def create_new_submenu(menu_id: str, submenu: SubMenuCreate, service: SubMenuCache = Depends(submenu_service)) -> SubMenuOut:
    return await service.create_submenu(menu_id, submenu)

@router.patch('/{menu_id}/submenus/{submenu_id}', response_model=SubMenuOut, status_code=200, tags=['Submenu'])
async def to_update_submenu(submenu_id: str, obj_in: SubMenuUpdate, service: SubMenuCache = Depends(submenu_service)) -> SubMenuOut:
    return await service.update_submenu(submenu_id, obj_in)

@router.delete('/{menu_id}/submenus/{submenu_id}', response_model=StatusMessage, status_code=200, tags=['Submenu'])
async def to_delete_submenu(submenu_id: str, service: SubMenuCache = Depends(submenu_service)) -> StatusMessage:
    return await service.delete_submenu(submenu_id)

# CRUD dish
@router.get('/{menu_id}/submenus/{submenu_id}/dishes', response_model=list[DishOut], status_code=200, tags=['Dish'])
async def get_all_dishes(submenu_id: str, service: DishCache = Depends(dish_service)) -> list[DishOut]:
    print('--------------------- 58')
    return await service.get_dish_list(submenu_id)

@router.get('/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', response_model=DishOut, status_code=200, tags=['Dish'])
async def get_one_dish(dish_id: str, service: DishCache = Depends(dish_service)) -> DishOut:
    return await service.get_dish(dish_id)

@router.post('/{menu_id}/submenus/{submenu_id}/dishes', response_model=DishOut, status_code=201, tags=['Dish'])
async def create_new_dish(submenu_id: str, dish: DishCreate, service: DishCache = Depends(dish_service)) -> DishOut:
    print('--------------------- 67')
    print(submenu_id)
    return await service.create_dish(submenu_id, dish)

@router.patch('/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', response_model=DishOut, status_code=200, tags=['Dish'])
async def to_update_dish(dish_id: str, obj_in: DishUpdate, service: DishCache = Depends(dish_service)) -> DishOut:
    return await service.update_dish(dish_id, obj_in)

@router.delete('/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', response_model=StatusMessage, status_code=200, tags=['Dish'])
async def to_delete_dish(dish_id: str, service: DishCache = Depends(dish_service)) -> StatusMessage:
    return await service.delete_dish(dish_id)
