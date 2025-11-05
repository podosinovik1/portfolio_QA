import pytest

from settings import ENDPOINTS
from conftest import (
    get_request,
    post_request,
    put_request,
    delete_request,
)

class ObjectClient:
    """
    API client for Objects endpoints.
    
    Provides methods for CRUD operations on objects:
    - Retrieve all objects or by ID(s)
    - Create new objects
    - Update existing objects  
    - Delete objects
    """
    def __init__(
            self, 
            get_request, 
            post_request,
            put_request,
            delete_request,
        ):
        """
        Initialize ObjectClient with request fixtures.
        
        Args:
            get_request: Fixture for GET requests
            post_request: Fixture for POST requests  
            put_request: Fixture for PUT requests
            delete_request: Fixture for DELETE requests
        """
        self._get = get_request
        self._post = post_request
        self._put = put_request
        self._delete = delete_request
        self.base = ENDPOINTS["objects"]

    def get_all(self):
        """GET all objects.
        
        Returns:
            Response object with list of all objects
        """
        return self._get(endpoint=self.base)
    
    def get_by_id(self, object_id):
        """GET specific object by ID.
        
        Args:
            object_id: Unique identifier of the object
            
        Returns:
            Response object with requested object data
        """
        return self._get(endpoint=f"{self.base}/{object_id}")

    def get_list_by_ids(self, id_list):
        """GET multiple objects by list of IDs.
        
        Args:
            id_list: List of object IDs to retrieve
            
        Returns:
            Response object with list of requested objects
        """
        ids = {"id": id_list}
        return self._get(
            endpoint=self.base, 
            params=ids
            )
    
    def post_object(self, payload):
        """POST new object.
        
        Args:
            payload: Dictionary with object data for creation
            
        Returns:
            Response object with created object data
        """
        return self._post(
            endpoint=self.base, 
            payload=payload,
            )

    def update_object(self, payload, object_id):
        """PUT update existing object.
        
        Args:
            payload: Dictionary with updated object data
            object_id: ID of object to update
            
        Returns:
            Response object with updated object data
        """
        return self._put(
            endpoint=f"{self.base}/{object_id}",
            payload=payload
        )

    def delete_object(self, object_id):
        """DELETE object by ID.
        
        Args:
            object_id: ID of object to delete
            
        Returns:
            Response object from delete operation
        """
        return self._delete(
            endpoint=f"{self.base}/{object_id}",
            payload=None
            )


@pytest.fixture
def object_client(get_request, post_request, put_request, delete_request):
    """
    Fixture providing ObjectClient instance for testing.
    
    Args:
        get_request: GET request fixture
        post_request: POST request fixture  
        put_request: PUT request fixture
        delete_request: DELETE request fixture
        
    Returns:
        ObjectClient: Configured client for objects API endpoints
    """
    return ObjectClient(get_request, post_request, put_request, delete_request)
