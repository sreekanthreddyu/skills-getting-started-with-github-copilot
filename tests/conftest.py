import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module
from src.app import app


@pytest.fixture(scope="session")
def baseline_activities():
    return copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities(baseline_activities):
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(baseline_activities))
    yield


@pytest.fixture()
def client():
    return TestClient(app)
