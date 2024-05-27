import os

from src.core.constants import MIGRATION_PATH
from src.core.database.database import Database


class Migrator:
    def __init__(self, db: Database):
        self.db = db
        files = os.listdir(MIGRATION_PATH)
        migration_files = dict()

        for file in files:
            if file.endswith(".sql"):
                migration_files[int(file.split(".sql")[0].split("_")[-1])] = file

        self.last_migration = migration_files[max(migration_files.keys())]

    async def make_migration(self):
        with open(f"{MIGRATION_PATH}/{self.last_migration}", "r") as f:
            raw_sql = f.read()
            conn = await self.db.get_connection()
            await conn.execute(raw_sql)
