import jwt

from src.app.services.user_service import UserService
from unittest.mock import Mock
from jwt.exceptions import InvalidTokenError


@pytest.fixture
def user_repository_mock():
    return Mock(name="user_repository_mock")


@pytest.fixture
def user_service_fixture(user_repository_mock):
    return UserService(user_repository_mock, secret_key="secret")


def test_user_service_get_current_user_happy_path(user_service_fixture, mocker):
    # Preparation
    mock_jwt = mocker.patch("src.app.services.user_service.jwt")
    mock_jwt.decode.side_effect = jwt.exceptions.DecodeError

    # Execution
    result = user_service_fixture.get_current_user("test_token")

    #Assertions
    mock_jwt.decode.assert_called_with("test_token", "secret", algorithms=[user_service_fixture.ALGORITHM])
    user_repository_mock.get_user_db.assert_called_with("test_user")
    assert result == "test_user"


def test_user_service_get_current_user_wrong_token(user_service_fixture, mocker):
    # Preparation
    mock_jwt = mocker.patch("src.app.services.user_service.jwt")
    mock_jwt.decode.side_effect = InvalidTokenError

    # Execution
    with pytest.raises(HTTPException):
        user_service_fixture.get_current_user("test_token")

    # Assertions
    mock_jwt.decode.assert_called_with("test_token", "secret", algorithms=[user_service_fixture.ALGORITHM])
    user_repository_mock.get_user_db.assert_not_called()