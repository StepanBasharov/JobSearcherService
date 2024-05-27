import hashlib

from app.domain.user.errors.user_input_errors import (
    PasswordToShortError,
    SamePasswordEmail
)


class PasswordManager:
    def __init__(self, password: str, email: str = None):
        self.password = password
        self.email = email

    def _validate_password_len(self):
        if len(self.password) < 8:
            raise PasswordToShortError

    def _validate_password_email(self):
        if self.password == self.email:
            raise SamePasswordEmail

    def execute(self) -> str:
        if self.email:
            self._validate_password_len()
            self._validate_password_email()

        return hashlib.sha256(self.password.encode('utf-8')).hexdigest()
