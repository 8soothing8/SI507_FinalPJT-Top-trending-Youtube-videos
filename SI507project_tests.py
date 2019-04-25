import unittest
import sqlite3
from SI507project_tools import *

class Cache(unittest.TestCase):
    def test_cache_diction(self):
        self.assertIsInstance(CACHE_DICTION, dict,"Cached file is a dictionary type")
    def test_cache_contents(self):
        testfile = open("SI507finalproject_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue(len(testfilestr)>0, "Cached file contains results")

class APIcall(unittest.TestCase):
    def test_api_result(self):
        self.assertIsInstance(popular_video_list, list, "Newly called file is a list type")

class DBTests(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect("youtube_popular_videos.db")
        self.cur = self.conn.cursor()


if __name__ == "__main__":
    unittest.main(verbosity=3)
