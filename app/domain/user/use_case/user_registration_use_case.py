from app.domain.user.interfaces.use_case_interfaces import UseCaseInterface
from app.domain.user.repository.user_repository import UserRepository
from app.domain.user.schemas.request_schemas import RegistrationRequest
from app.domain.user.schemas.response_schemas import RegistrationResponse


class RegistrationUseCase(UseCaseInterface):
    def __init__(self, request: RegistrationRequest):
        self.repository = UserRepository()
        self.request = request

    async def execute(self) -> RegistrationResponse:
        await self.repository.create_new_user(
            first_name=self.request.first_name,
            last_name=self.request.last_name,
            patronymic=self.request.patronymic,
            age=self.request.age,
            date_of_birth=self.request.date_of_birth,
            living=self.request.living,
            email=self.request.email,
            phone=self.request.phone,
            password=self.request.password,
        )

        new_user = await self.repository.get_user_by_email(email=self.request.email)

        return RegistrationResponse(id=new_user.id, result=True, time=1)
