from unittest import TestCase
from client_test import client


class TestModelPrediction(TestCase):
    def test_sucess(self):
        data = {"feature1": 3.14,"feature2": 3.14}
        response = client.post("/predict", json=data)        
        self.assertEqual(response.status_code, 200)
    
    def test_error_payload(self):
        data = {"feature1": "a string","feature2": "other string"}
        response = client.post("/predict", json=data)        
        self.assertEqual(response.status_code, 422)
        