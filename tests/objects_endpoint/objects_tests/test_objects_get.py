import pytest

from settings import (
    OK,
    NOT_FOUND, BAD_REQUEST
)

from objects_endpoint.fixtures.fixture_object import (
    object_client,
)


@pytest.mark.objects
class TestObjectGET:
    """Test suite for GET api/Objects endpoints."""

    @pytest.fixture(autouse=True)
    def setup(self, object_client):
        """Initialize API client for object endpoints."""
        self.client = object_client

    def test_get_all_objects(self):
        """TEST: Retrieve all objects and validate response structure."""
        response = self.client.get_all()

        assert response.status_code == OK, (
            f"Expected {OK}, Got {response.status_code}",
            f"Message: {response.text}"
        )

        assert isinstance(response.json(), list) == True, (
            f"{response.json()}"
        )
        assert isinstance(response.json()[0], dict) == True, (
            f"{response.json()}"
        )

    @pytest.mark.parametrize(
        ("object_id_list", "expected_http_code"),
        (
            ([1, 2, 3], OK),  # Valid ID list
        )
    )
    def test_get_list_by_ids(self, object_id_list, expected_http_code):
        """TEST: Get objects by ID list and validate response format."""
        param = object_id_list
        response = self.client.get_list_by_ids(id_list=param)

        assert response.status_code == expected_http_code, (
        f"Expected {expected_http_code}, Got {response.status_code}",
        f"Message: {response.text}"
        )

        if response.status_code == OK:
            assert isinstance(response.json(), list) == True, (
                f"{response.json()}"
            )
            assert isinstance(response.json()[0], dict) == True, (
                f"{response.json()}"
            )


    @pytest.mark.parametrize(
        ("object_id", "expected_http_code"),
        (
            (1, OK),     # Valid ID
            (0, NOT_FOUND),  # Zero ID
            (-1, NOT_FOUND), # Negative ID
            pytest.param(
                True, BAD_REQUEST,
                marks=pytest.mark.xfail(reason="API doesn't validate type ID")
            )
        )
    )
    def test_get_by_id(self, object_id, expected_http_code):
        """TEST: Get object by ID with validation."""
        response = self.client.get_by_id(object_id=object_id)

        assert response.status_code == expected_http_code, (
        f"Expected {expected_http_code}, Got {response.status_code}",
        f"Message: {response.text}"
        )
        
        if response.status_code == OK:
            required_keys = {"id", "name", "data"}
            response_data = response.json()
            response_keys = set(response_data.keys())
            lost_keys = required_keys - response_keys

            assert lost_keys == set(), (
                f"Lost keys of response data: {lost_keys}"
            )