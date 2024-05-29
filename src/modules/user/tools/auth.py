import jwt
import datetime

from src.core.conf.config import Config


class Auth:
    @staticmethod
    def create_token(user_id: int) -> str:
        conf = Config.new_config()
        auth_conf = conf.get_server_auth_conf

        payload = {
            "user_id": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=auth_conf.exp_time)
        }

        token = jwt.encode(payload, auth_conf.secret, algorithm=auth_conf.algorithm)

        return token
