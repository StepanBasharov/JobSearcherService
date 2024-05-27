from datetime import date

from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    firstname: str
    lastname: str
    patronymic: str | None
    age: int | None
    email: str
    phone: str
    password: str
    dateofbirth: date | None
    living: str | None
    profession_id: int | None
