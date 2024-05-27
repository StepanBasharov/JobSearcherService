from src.domain.user.errors.user_input_errors import UnAuthorizationError
from src.domain.user.interfaces.use_case_interfaces import UseCaseInterface
from src.domain.user.schemas.request_schemas import LoginRequest
from src.domain.user.repository.user_repository import UserRepository
from src.domain.user.tools.password_manager import PasswordManager


class LoginUseCase(UseCaseInterface):
    def __init__(self, request: LoginRequest):
        self.request = request
        self.repository = UserRepository()
        self.password_manager = PasswordManager(password=self.request.password)

    async def execute(self):
        user = await self.repository.get_user_by_email_or_phone(login=self.request.login)
        if user.password != self.password_manager.execute():
            raise UnAuthorizationError
        return user
