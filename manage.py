from app.core.server.server import Server
from app.core.conf.config import Config
from app.repository.repo import Repository

if __name__ == "__main__":
    config = Config.new_config()
    server = Server(
        *config.get_server_conf,
        repo=Repository(config=config)
    )
    server.start_server()
