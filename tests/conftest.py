import os
import sys
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from testapp.server import app


@pytest.fixture
def tapp():
    return app.test_client()
