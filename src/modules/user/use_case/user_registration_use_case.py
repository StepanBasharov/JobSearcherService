from src.core.interfaces.user_interfaces.use_case_interfaces import UseCaseInterface
from src.modules.user.repository.user_repository import UserRepository
from src.modules.user.schemas.request_schemas import RegistrationRequest
from src.modules.user.schemas.response_schemas import RegistrationResponse
from src.modules.user.tools.password_manager import PasswordManager


class RegistrationUseCase(UseCaseInterface):

    def __init__(self, request: RegistrationRequest):
        self.request = request
        self.repository = UserRepository()
        self.password_manager = PasswordManager(
            password=self.request.password,
            email=self.request.email
        )

    async def execute(self) -> RegistrationResponse:
        password = self.password_manager.execute()
        await self.repository.create_new_user(
            first_name=self.request.first_name,
            last_name=self.request.last_name,
            patronymic=self.request.patronymic,
            age=self.request.age,
            date_of_birth=self.request.date_of_birth,
            living=self.request.living,
            email=self.request.email,
            phone=self.request.phone,
            password=password,
        )

        new_user = await self.repository.get_user_by_email(email=self.request.email)

        return RegistrationResponse(id=new_user.id, result=True)
