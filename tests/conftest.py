"""Package-wide test fixtures."""
from unittest.mock import Mock

from _pytest.config import Config
import pytest
from pytest_mock import MockFixture


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    """Pytest configuration hook."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock


def pytest_configure(config: Config) -> None:
    """Fixture for mocking requests.get."""
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")
