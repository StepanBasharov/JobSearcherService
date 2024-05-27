from app.core.base_error import BaseError


class PasswordToShortError(BaseError):
    message = "Пароль дольжен состоять минимум из 8 символов"
    status_code = 400


class SamePasswordEmail(BaseError):
    message = "Пароль и email не должны совпадать"
    status_code = 400
