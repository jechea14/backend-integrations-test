import unittest

from app import app


class AppTestCase(unittest.TestCase):

    def test_ping(self):
        tester = app.test_client(self)
        response = tester.get('/ping')
        assert 'PONG' in response.data
        
    def test_get_token(self):
        pass
    
    def test_product(self):
        pass
    
    def test_merchants(self):
        pass
    
    def test_update_merchant(self):
        pass


if __name__ == '__main__':
    unittest.main()
