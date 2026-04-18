from api.backend_client import BackendClient
from api.core_client import CoreClient
from db.db_client import Database, DatabaseClient
import pytest


@pytest.fixture(scope="session")
def backend_client():
    core_client = CoreClient()
    backend_client = BackendClient(core_client)
    yield backend_client
    core_client.close()


@pytest.fixture(scope="session")
def db():
    client = DatabaseClient()
    db = Database(client)
    yield db
    client.close()
