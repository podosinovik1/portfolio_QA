import pytest

from settings import ENDPOINTS
from conftest import (
    get_request,
    post_request,
    put_request
)


class ObjectClient:
    def __init__(
            self, 
            get_request, 
            post_request,
            put_request,
        ):
        self._get = get_request
        self._post = post_request
        self._put = put_request
        self.base = ENDPOINTS["objects"]

    def get_all(self):
        return self._get(endpoint=self.base)
    
    def get_by_id(self, object_id):
        return self._get(endpoint=f"{self.base}/{object_id}")

    def get_list_by_ids(self, id_list):
        ids = {"id": id_list}
        return self._get(
            endpoint=self.base, 
            params=ids
            )
    
    def post_object(self, payload):
        return self._post(
            endpoint=self.base, 
            payload=payload,
            )

    def update_object(self, payload, object_id):
        return self._put(
            endpoint=f"{self.base}/{object_id}",
            payload=payload
        )


@pytest.fixture
def object_client(get_request, post_request, put_request):
    return ObjectClient(get_request, post_request, put_request)
