import pytest

from settings import (
    OK,
    BAD_REQUEST, CONFLICT, UNPROCESSABLE
)

from objects_endpoint.fixtures.fixture_object import (
    object_client,
)
from objects_endpoint.cases.objects_cases import (
    payload,
)

@pytest.mark.parametrize(
    ("case", "expected_http_code"),
    (
        # Valid cases - should return 200 OK
        ("valid_data", (OK,)),
        
        # Invalid cases - should return error codes
        pytest.param(
            "invalid_name", (BAD_REQUEST, CONFLICT, UNPROCESSABLE),
            marks=pytest.mark.xfail(reason="API doesn't validate 'name'")
        ),
        pytest.param(
            "invalid_year", (BAD_REQUEST, CONFLICT, UNPROCESSABLE),
            marks=pytest.mark.xfail(reason="API doesn't validate 'year'")
        ),
        pytest.param(
            "invalid_price", (BAD_REQUEST, CONFLICT, UNPROCESSABLE),
            marks=pytest.mark.xfail(reason="API doesn't validate 'price'")
        ),
    )
)
@pytest.mark.objects
class TestObjectPOSTandPUT:
    """Test suite for POST, PUT api/Objects endpoints."""

    @pytest.fixture(autouse=True)
    def setup(self, object_client):
        """Initialize API client for object endpoints."""
        self.client = object_client

    def test_post_object(
            self,
            case,
            expected_http_code
        ):
        
        payload_data = payload(case)

        response = self.client.post_object(payload_data)

        assert response.status_code in expected_http_code, (
        f"Expected {expected_http_code}, Got {response.status_code}",
        f"Message: {response.text}"
        )

        if response.status_code == OK:
            required_keys = {"id", "name", "data", "createdAt"}
            response_data = response.json()
            response_keys = set(response_data.keys())
            lost_keys = required_keys - response_keys
        
            obj_id = response.json()["id"]
            response_put = self.client.update_object(
                payload_data,
                obj_id
            )
            assert response_put.status_code in expected_http_code, (
            f"Expected {expected_http_code}, Got {response_put.status_code}",
            f"Message: {response_put.text}"
        )
