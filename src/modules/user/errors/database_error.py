from src.core.base_error import BaseError


class AlreadyExistsError(BaseError):
    message = "Пользователь с таким номером или email уже существует"
    status_code = 409


class UserNotFoundError(BaseError):
    message = "Пользователь не найдет"
    status_code = 404
