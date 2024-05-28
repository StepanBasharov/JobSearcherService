from src.modules.user.errors.user_input_errors import UnAuthorizationError
from src.core.interfaces.user_interfaces.use_case_interfaces import UseCaseInterface
from src.modules.user.schemas.request_schemas import LoginRequest
from src.modules.user.repository.user_repository import UserRepository
from src.modules.user.tools.password_manager import PasswordManager


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
