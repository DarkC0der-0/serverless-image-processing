import unittest
from app import app, db
from app.models import Image

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_upload_image(self):
        with open('test/test_image.jpg', 'rb') as img:
            response = self.app.post('/upload', data={'image': img})
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
