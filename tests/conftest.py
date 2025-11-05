import pytest
import requests
import json

from settings import BASE_URL, ENDPOINTS, TIMEOUT


def _serialization(data: dict):
    try:
        return json.dumps(data)
    except (TypeError, ValueError, OverflowError) as e:
        pytest.fail(f"JSON serialization error: {e}")


@pytest.fixture
def get_request():
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