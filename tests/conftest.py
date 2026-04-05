from api_client import ApiClient
from db.db_client import DB, DBClient
import pytest


@pytest.fixture(scope="session")
def client():
    client = ApiClient()
    yield client
    client.close()


@pytest.fixture(scope="session")
def db():
    client = DBClient()
    db = DB(client)
    yield db
    client.close()
