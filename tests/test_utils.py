import unittest
from app.utils import process_image

class UtilsTestCase(unittest.TestCase):
    def test_process_image(self):
        with open('test/test_image.jpg', 'rb') as img:
            processed = process_image(img.read())
            self.assertEqual(processed)

if __name__ == '__main__':
    unittest.main()
    