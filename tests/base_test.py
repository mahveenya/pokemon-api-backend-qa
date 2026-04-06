from api.api_client import Client
from db.db_client import Database
import pytest


class BaseTest:
    db: Database
    client: Client

    @pytest.fixture(autouse=True)
    def setup(self, client, db):
        self.db = db
        self.client = client
