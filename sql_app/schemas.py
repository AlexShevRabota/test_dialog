from pydantic import BaseModel


class RestaurantTableBase(BaseModel):
    title: str
    description: str | None = None


class RestaurantTableCreate(RestaurantTableBase):
    pass


class RestaurantTable(RestaurantTableBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str



class UserCreate(UserBase):
    password: str
    phone: str
    name: str
    surname: str


class User(UserBase):
    id: int
    items: list[RestaurantTable] = []

    class Config:
        orm_mode = True
