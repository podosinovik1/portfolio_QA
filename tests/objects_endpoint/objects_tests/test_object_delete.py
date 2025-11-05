import pytest

from settings import (
    OK,
)

from objects_endpoint.fixtures.fixture_object import (
    object_client,
)
from objects_endpoint.cases.objects_cases import (
    payload,
)


@pytest.mark.objects
class TestObjectDELETE:
    """Test suite for DELETE api/Objects endpoints."""

    @pytest.fixture(autouse=True)
    def setup(self, object_client):
        """Initialize API client for object endpoints."""
        self.client = object_client

    def test_delete_by_id(self):
        """TEST: Delete object by ID after creation.
        
        Verifies successful object deletion workflow:
        1. Create object with valid payload
        2. Extract object ID from response
        3. Delete object by ID
        4. Verify 200 OK response
        """
        payload_data = payload("valid_data")
        response = self.client.post_object(payload_data)
        obj_id = response.json()["id"]

        delete = self.client.delete_object(obj_id)

        assert delete.status_code == OK, (
            f"Expected {OK}, Got {delete.status_code}",
            f"Message: {delete.text}"
        )