import pytest
import requests
import json

from settings import BASE_URL, ENDPOINTS, TIMEOUT


def _serialization(data: dict):
    """
    Serialize dictionary to JSON string with error handling.
    
    Args:
        data: Dictionary to serialize
        
    Returns:
        JSON string representation of data
        
    Raises:
        pytest.fail: If serialization fails due to non-serializable data
    """
    try:
        return json.dumps(data)
    except (TypeError, ValueError, OverflowError) as e:
        pytest.fail(f"JSON serialization error: {e}")


@pytest.fixture
def get_request():
    """
    Fixture for making GET HTTP requests.
    
    Returns:
        Function that performs GET request with error handling
        
    Steps:
        1. Construct full URL from BASE_URL and endpoint
        2. Send GET request with parameters and headers
        3. Handle connection and timeout errors
        4. Return response object
    """
    def _get_request(
            endpoint, 
            params=None,
            headers=None
            ):
        try:
            response = requests.get(
                url=f"{BASE_URL}{endpoint}",
                params=params,
                headers=headers,
                timeout=TIMEOUT,
            )
            return response
        
        except ConnectionError as e:
            pytest.fail(f"Connection error: {e}")
        except TimeoutError as e:
            pytest.fail(f"Timeout: {e}")
        except Exception as e:
            pytest.fail(f"Request failed: {e}")
    
    return _get_request


@pytest.fixture
def post_request():
    """
    Fixture for making POST HTTP requests.
    
    Returns:
        Function that performs POST request with JSON serialization
        
    Steps:
        1. Set Content-Type header to application/json if not provided
        2. Serialize payload to JSON string
        3. Send POST request with JSON data
        4. Handle connection and timeout errors
        5. Return response object
    """
    def _post_request(
            endpoint,
            payload,
            headers=None,
    ):
        if headers == None:
            headers = {}
            headers["Content-type"] = "application/json"
        
        payload = _serialization(payload)
        
        try:
            response = requests.post(
                url=f"{BASE_URL}{endpoint}",
                data=payload,
                headers=headers,
                timeout=TIMEOUT
            )
            return response
        
        except ConnectionError as e:
            pytest.fail(f"Connection error: {e}")
        except TimeoutError as e:
            pytest.fail(f"Timeout: {e}")
        except Exception as e:
            pytest.fail(f"Request failed: {e}")
    
    return _post_request


@pytest.fixture
def put_request():
    """
    Fixture for making PUT HTTP requests.
    
    Returns:
        Function that performs PUT request with JSON serialization
        
    Steps:
        1. Set Content-Type header to application/json if not provided
        2. Serialize payload to JSON string
        3. Send PUT request with JSON data
        4. Handle connection and timeout errors
        5. Return response object
    """
    def _put_request(
            endpoint,
            payload,
            headers=None,
    ):
        if headers == None:
            headers = {}
            headers["Content-type"] = "application/json"
        
        payload = _serialization(payload)

        try:
            response = requests.put(
                url=f"{BASE_URL}{endpoint}",
                data=payload,
                headers=headers,
                timeout=TIMEOUT
            )
            return response
        
        except ConnectionError as e:
            pytest.fail(f"Connection error: {e}")
        except TimeoutError as e:
            pytest.fail(f"Timeout: {e}")
        except Exception as e:
            pytest.fail(f"Request failed: {e}")
    
    return _put_request


@pytest.fixture
def delete_request():
    """
    Fixture for making DELETE HTTP requests.
    
    Returns:
        Function that performs DELETE request
        
    Steps:
        1. Send DELETE request with JSON payload
        2. Handle connection and timeout errors
        3. Return response object
    """
    def _delete_request(payload, endpoint, headers=None):
        try:
            response = requests.delete(
                url=f"{BASE_URL}{endpoint}",
                json=payload,
                headers=headers,
                timeout=TIMEOUT,
            )
            return response

        except ConnectionError as e:
            pytest.fail(f"Connection error: {e}")
        except TimeoutError as e:
            pytest.fail(f"Timeout: {e}")
        except Exception as e:
            pytest.fail(f"Request failed: {e}")
    
    return _delete_request