import os

from app.core.constants import MIGRATION_PATH
from interfaces.repo_interfaces import RepositoryInterface


class Migrator:
    def __init__(self, repository: RepositoryInterface):
        self.repo = repository
        files = os.listdir(MIGRATION_PATH)
        print(files)
        migration_files = dict()

        for file in files:
            if file.endswith(".sql"):
                migration_files[int(file.split(".sql")[0].split("_")[-1])] = file

        self.last_migration = migration_files[max(migration_files.keys())]

    async def make_migration(self):
        with open(f"{MIGRATION_PATH}/{self.last_migration}", "r") as f:
            raw_sql = f.read()
            await self.repo.sql_execute(raw_sql)
