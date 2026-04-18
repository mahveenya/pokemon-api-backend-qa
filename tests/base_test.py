from api.backend_client import BackendClient
from db.db_client import Database
import pytest


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, backend_client: BackendClient, db: Database):
        self.db = db
        self.backend_client = backend_client
