#!/usr/bin/env python

import unittest
import artists

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.app = artists.app.test_client()

    def test_show_home_page_title(self):
        response = self.app.get('/')
        self.assertIn('Artist Search', response.data.decode())

    def test_show_search_result_after_post(self):
        response = self.app.post('/', data={"artist":"Queen"})

        self.assertIn('Queen', response.data.decode())
        self.assertNotIn('Oasis', response.data.decode())

if __name__ == '__main__':
    unittest.main()
