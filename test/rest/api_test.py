import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/5/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/12/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide_error_zero(self):
        url = f"{BASE_URL}/calc/divide/2/0"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        self.assertEqual(cm.exception.status,  http.client.BAD_REQUEST)
    
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_sqrt_error_negative_number(self):
        url = f"{BASE_URL}/calc/sqrt/-10"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        self.assertEqual(cm.exception.status,  http.client.BAD_REQUEST)
    
    def test_api_logbase10(self):
        url = f"{BASE_URL}/calc/logbase10/1000"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_logbase10_error_zero(self):
        url = f"{BASE_URL}/calc/logbase10/0"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        self.assertEqual(cm.exception.status,  http.client.BAD_REQUEST)
    
    def test_api_logbase10_error_string(self):
        url = f"{BASE_URL}/calc/logbase10/cero"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        self.assertEqual(cm.exception.status,  http.client.BAD_REQUEST)
