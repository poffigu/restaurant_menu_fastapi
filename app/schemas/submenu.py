from pydantic import BaseModel


class SubmenuBase(BaseModel):
    title: str
    description: str


class SubmenuCreate(SubmenuBase):
    # menu_id: str | None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "string",
                "description": "string",
            },
        }


class SubmenuUpdate(SubmenuBase):
    class Config:
        json_schema_extra = {
            "example": {
                "title": "string",
                "description": "string",
            },
        }


class SubmenuOut(SubmenuBase):
    id: str
    dishes_count: int

    class Config:
        from_attributes = True
