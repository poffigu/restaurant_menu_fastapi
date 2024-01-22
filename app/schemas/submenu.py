from pydantic import BaseModel


class SubMenuBase(BaseModel):
    title: str
    description: str


class SubMenuCreate(SubMenuBase):
    # menu_id: str | None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "string",
                "description": "string",
            },
        }


class SubMenuUpdate(SubMenuBase):
    class Config:
        json_schema_extra = {
            "example": {
                "title": "string",
                "description": "string",
            },
        }


class SubMenuOut(SubMenuBase):
    id: str
    dishes_count: int

    class Config:
        from_attributes = True
