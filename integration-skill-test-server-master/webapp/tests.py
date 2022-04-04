import unittest
import json
from app import app
import os

GRAND_TYPE = ["client_credentials", "refresh_token"]
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
RICHARD_ID = os.environ.get("RICHARD_ID")
BEAUTY_ID = os.environ.get("BEAUTY_ID")


class AppTestCase(unittest.TestCase):

    def test_ping(self):
        tester = app.test_client(self)
        response = tester.get('/ping')
        assert b'PONG' in response.data

    def test_get_token(self):
        mock_params = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': GRAND_TYPE
        }

        tester = app.test_client(self)
        response = tester.post('/oauth/token', query_string=mock_params)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_product(self):
        mock_request_headers = {
            'token': 'Bearer JcJTkYYkJJYYhYTcAjkZ',
            'Content-Type': 'application/json'
        }

        mock_request_data = {
            "merchant_id": RICHARD_ID,
            "sku": "251261",
            "barcodes": ["72649244"],
            "brand": "Lubritek",
            "name": "Toallita Humeda C/30 Pzas",
            "description": "Toallita Humeda C30 Pzas 1 Pza",
            "package": "1 PZA",
            "image_url": "https://locahost:8000/images/72649244?height=500&width=500",
            "category": "Hardlines | Sporting Goods | Piscina & Juegos Agua",
            "url": None,
            "branch_products": [{
                "branch": "MM",
                "stock": 4,
                "price": 90.3
            }
            ]
        }

        tester = app.test_client(self)
        response = tester.post(
            '/api/products', json=json.dumps(mock_request_data), headers=mock_request_headers)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_merchants(self):
        mock_request_headers = {
            'token': 'Bearer JcJTkYYkJJYYhYTcAjkZ'
        }
        tester = app.test_client(self)
        response = tester.get('/api/merchants', headers=mock_request_headers)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_update_merchant(self):
        mock_request_headers = {
            'token': 'Bearer JcJTkYYkJJYYhYTcAjkZ',
            'Accept': '*/*'
        }

        mock_request_data = {
            "id": "ae9c81fe-163e-4546-8349-19dbf63715c7",
            "name": "Richard's",
            "is_active": True,
            "can_be_updated": True,
            "can_be_deleted": False
        }

        tester = app.test_client(self)
        response = tester.put('/api/merchants/ae9c81fe-163e-4546-8349-19dbf63715c7',
                              json=json.dumps(mock_request_data), headers=mock_request_headers, content_type='application/json')

        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == '__main__':
    unittest.main()
