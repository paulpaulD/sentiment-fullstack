import unittest
import requests

class TestFlaskApp(unittest.TestCase):

    BASE_URL = 'http://localhost:5000'  # Adjust if your Flask app is running on a different URL or port

    def test_predict_positive(self):
        response = requests.post(f'{self.BASE_URL}/predict', json={'text': 'I love this product!'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('sentiment'), 'Positive')

    def test_predict_negative(self):
        response = requests.post(f'{self.BASE_URL}/predict', json={'text': 'I hate this product!'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('sentiment'), 'Negative')

    def test_predict_neutral(self):
        response = requests.post(f'{self.BASE_URL}/predict', json={'text': 'This product is okay.'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('sentiment'), 'Neutral')

    def test_predict_empty_text(self):
        response = requests.post(f'{self.BASE_URL}/predict', json={'text': ''})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get('error'), 'No text provided')

    def test_predict_no_text_field(self):
        response = requests.post(f'{self.BASE_URL}/predict', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get('error'), 'No text provided')

if __name__ == '__main__':
    unittest.main()
