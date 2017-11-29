"""
How to run this:
> python3 rest_apis/test_rest_api.py
"""

import json
import unittest

from rest_api import app


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        # self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        # app.init_db()

    def tearDown(self):
        # os.close(self.db_fd)
        # os.unlink(app.app.config['DATABASE'])
        pass

    def test_get(self):
        response = self.app.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode()), {'hello': 'world'})


if __name__ == '__main__':
    unittest.main()
