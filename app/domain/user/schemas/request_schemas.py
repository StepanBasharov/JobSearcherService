from datetime import date

from pydantic import BaseModel, Field


class RegistrationRequest(BaseModel):
    first_name: str = Field(description="Имя")
    last_name: str = Field(description="Фамилия")
    patronymic: str | None = Field(default=None, description="Отчество")
    age: int | None = Field(default=None, description="Возраст")
    date_of_birth: date | None = Field(default=None, description="Дата рождения")
    living: str | None = Field(default=None, description="Место проживания")
    email: str = Field(description="email")
    phone: str = Field(description="Телефон")
    password: str = Field(description="Пароль")
    

class LoginRequest(BaseModel):
    login: str = Field(description="Номер телефона или email")
    password: str = Field(description="Пароль")
