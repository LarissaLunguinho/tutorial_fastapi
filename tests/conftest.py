from typing import Generator
from fastapi.testclient import TestClient
import pytest

from main import app

# Fixture - Este decorador pode ser usado, com ou sem parâmetros
@pytest.fixture(scope='function')
def client() -> Generator:
    with TestClient(app) as c:
        yield c
